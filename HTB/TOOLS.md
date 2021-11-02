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
zip2john <zipfile> <output-hashfile>

john <output-hashfile>
```


## sqlmap

```
sqlmap -u "<url>" --cookie="<key=values>" --os-shell
```
