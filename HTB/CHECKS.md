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
