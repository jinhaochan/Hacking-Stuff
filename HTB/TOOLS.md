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

zip2john <file.zip> 2>/dev/null | tee <file.hash>

john <file.hash> --wordlist=/usr/share/wordlists/rockyou.txt --format=<format>

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

add --> http <ip> <port>

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

copy your pub key to the victim under `/home/user/.ssh/authorized_keys`

`ssh -i key -L 8000:127.0.0.1:8000 <user>@<ip>`

