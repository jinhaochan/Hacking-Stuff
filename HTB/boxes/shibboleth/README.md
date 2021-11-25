Shibboleth
---

## Steps

1. fuzzing paths, and ipmi exploit

We fuzz for the path `http://zabbix.shibboleth.htb` which gives us an admin login page

Looking at Zabbix docs, it uses ipmi, which requires port 623 UDP to be open

we use metasploit to get the hashes

```
$ msfconsole

$ use auxiliary/scanner/ipmi/ipmi_dumphashes

$ set RHOST 10.10.11.125

$ run
```

Getting the hash, we crack it to get the password of Administrator:ilovepumkinpie1


2. RCE

From the UI, we go to `Configuration->Hosts->Create`

Under the Key, we select `system.run[<reverse shell command>, nowait]`

This will call a reverse shell Zabbix and we can get the user flag


## Root flag

1. Database exploit

`find / -group zabbix 2>/dev/null | grep -v proc`

We can access `zabbix_server.conf`. Taking a look inside, we see credentials to the database.

After logging in to the database, we look at the version `mariadb 10.3.25` and find that there is a CVE-2021-27928

Simply do that, and you can get root shell

