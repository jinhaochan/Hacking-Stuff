cap
---

## Steps

1. Get FTP password

Navigate to `<host>/data/0` to get the FTP password from wireshark

2. Get user flag

That credential works with both FTP and SSH. You can get user flag there

## Root Flag

1. Capabilities

reading `'/var/www/html/app.py`, they use `setuid(0)`. This means that the python binary has `CAP_SETUID` capabilities set.

run `python3 -c 'import os; os.setuid(0); os.system("/bin/sh")'` to get root shell
