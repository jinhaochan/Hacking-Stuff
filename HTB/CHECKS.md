1. Check what groups you are in
    - `id` 
2. Find all binaries that this group can run
    - `find / -group <group> -type f 2>/dev/null`
3. Shows all command this user can run as sudo
    - `sudo -l`
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
    - `/etc/apache2/sites-enabled/*`
9. Check mail
    - `/var/mail`
    - `/var/spool/mail`
10. Check for most recently modified files
11. Check Processes running in /proc
```
for val in range(1,1000):
    try:
        with open("/proc/"+str(val)+"/cmdline", 'r') as f:
            lines = f.readlines()
            print(lines)
    except:
        pass
```
