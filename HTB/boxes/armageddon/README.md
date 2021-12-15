armageddon
---

## Steps

1. Drupal Vuln

run gobuster to see that we can access a few files. once of which tells us that it's a drupal app, and its a vulnerable version.

we can attack it with drupalgeddon 2

2. msfconsole

use msfconsole to run drupalgeddon to get a shell

3. brucetherealadmin

read `/sites/default/settings.php` to get mysql password

read from `users` table to get the hash, and crack it `booboo`

## Root Flag

1. sudo -l

brucetherealadmin can run `sudo snap`


https://gtfobins.github.io/gtfobins/snap/#sudo
