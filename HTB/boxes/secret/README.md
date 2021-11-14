secret
---

## Steps

1. Get the token for JWT signing

- download the entire folder
- git log
- git checkout the suspicious one
- get the keys

2. theadmin

looking at the code, it only checks for the value `'name':'theadmin'` to be authenticated as admin

craft a jwt with the value `'name':'theadmin'` and sign it with the key found earlier

2. /api/logs

looking at the source code, we see the any requests to `/api/logs?file=` will execute a shell command

we can inject commands by sending `; <my command>`

url encode a reverse shell, and we get a connection as dasith

cat `/home/dasith/user.txt`

## root flag

1. find SUID

```
$ find / -perm -u=s -type f 2>/dev/null
$ /opt/count
```

`/opt/count` reads a file and prints the count of words/lines

2. Trigger a crash

we see that valgrind does crash report analysis

the run `/opt/count` and read in `/root/root.txt` and trigger a crash

```
$ ps aux | grep count
$ kill -BUS <pid>
```

the crash data is located at `/var/crash/_opt_count.1000.crash`

3. getting data from the crash

```
$ apport-unpack _opt_count.1000.crash /tmp/crashed
$ cd /tmp/crash
$ strings CoreDump
```
find the root flag value in the CoreDump



