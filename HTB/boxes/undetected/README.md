undetected
---

## User

1. enumerate to find the vulnerable library 

2. Gain foothold through RCE

3. find a binary you can run in your group 

4. `cat` it and hex decode it to get the hash

5. crack the hash and gain user flag

## Root

1. enumerate to find a mail

2. find last modified apache2 module `/usr/lib/apache2/modules`

3. strings to find the hex command

5. reverse engineer the binary it to find the backdoor password
