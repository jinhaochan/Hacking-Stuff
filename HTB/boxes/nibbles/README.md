nibbles
---

## Steps

1. gobuster to discover directories and find php files

We find the page `admin.php`

2. Finding the user

Looking at the source of the website, we find that there is a user called `admin` in  `/content/private/user.xml`

2. guessing the password

This is the part i really hate, which is guess the password.

It's `admin:nibbles` on `/admin.php`

3. CVE and Reverse Shell

`My Image` plugin has a cve that allows you to upload a php file. 

We upload a simple shell, and send it a request to connect to our reverse shell

https://packetstormsecurity.com/files/133425/NibbleBlog-4.0.3-Shell-Upload.html

From there we can get the user flag

4. Root flag

`sudo -l` shows we can run `sudo ./monitor.sh`

`monitor.sh` is rewriteable, and we can rewrite the file to print out the root flag

```
echo "cat /root/root.txt" > monitor.sh

sudo ./monitor.sh
```


