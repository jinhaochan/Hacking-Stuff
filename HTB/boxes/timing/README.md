timing
---

## User

<details>
  <summary>Spoiler warning</summary>
  
1. enumerate to find a php file that that has 0 bytes

2. `?img=php://filter/convert.base64-encode/resource=` to find users

3. login with <user>:<user>

4. examine how upload.php works

5. upload your malicious file and bruteforce the filename by generating the filenames simultaneously while uploading the file
  
6. Gain foothold via reverse shell
  
7. git log backup file to get password and user flag
  
</details>

## Root

<details>
  <summary>Spoiler warning</summary>
  
1. sudo -l
  
2. try to request something from your own server to see which binary it's running
  
3. modify the behavior of the binary with a config file e.g. `.binaryrc`
  
4. write to `authorized_keys` and gain root flag
  
</details>
