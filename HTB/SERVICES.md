Commands for regular services
---

## nmap

```
scan and show OS
---
nmap <addr> -sV
```


## FTP

ports
- 21
- 22

```
to determine if anonymous login is allowed during nmap
---
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
...

anonymous login
---
> ftp
> open <addr>

username = anonymous
password = <empty>

```

## SMB

ports
- 445
- 139

```
Listing shares
---
> smbcleint -L <addr>

$ at the end of the share means its an Administrative share

Connecting to a share
---
> smbclient //<addr>/WorkShares
```

## RDP

```
sometimes the password can be blank (just press enter)
---
xfreerdp /v:<addr> /cert:ignore /u:<user>
```

## MySQL

```
logging on with root does not require password
---
mysql -u root -h <remote server addr> 
```
