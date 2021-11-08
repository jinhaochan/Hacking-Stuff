Default credentials
---

```
id
---
Check what groups you are in

find / -group <group> -type f 2>/dev/null
---
find all binaries that this group can run

sudo -l
---
shows all command this user can run as sudo


find / -perm -u=s -type f 2>/dev/null
---
find all binaries with sticky bit set
```
