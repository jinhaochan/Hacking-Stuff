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

