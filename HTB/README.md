# General Approach to HTB

After you have obtained the target IP address, these are some general approaches

## 1. Footprinting target

Subdomain Discovery
1. Map a domain to the IP address in `/etc/hosts`
2. run `wfuzz -w SecLists/Discovery/DNS/subdomains-top1million-20000.txt -H "Host: FUZZ.<domain>"  -u 'http://<domain>' --hh <word size>`

Path Discovery
1. `gobuster dir -u <addr> -w /usr/share/wordlist/dirb/common.txt`

File Discovery
1. `gobuster dir -x php -u 10.129.255.70 -w /usr/share/wordlists/dirb/common.txt`


## 2. Service discovery

Find running services
1. `nmap -sV -p- <target>`
2. `nmap -sU -v <target>`

Find running versions
1. CMS
2. Database
3. Webserver
4. etc

## 3. Vulnerability Discovery

For each service running and their versions find related vulnerabilities to gain access to the server (draw the rest of the fucking owl)

[Non-exhuastive exploits](https://github.com/jinhaochan/HTB/blob/master/HTB/EXPLOITS.md)

Typically involves running a reverse shell
- [Web Shells](https://github.com/jinhaochan/HTB/blob/master/HTB/EXPLOITS.md#webshells)
- [Reverse Shells](https://github.com/jinhaochan/HTB/blob/master/HTB/EXPLOITS.md#nc-reverse-shells)

## 4. Privilege Escalation

Once on the server:
1. Run [Checks](https://github.com/jinhaochan/HTB/blob/master/HTB/CHECKS.md)
