# Stuff

nmap
1. `nmap -sSV -Pn -p- -A <target>`
2. `nmap -sU -v <target> --min-rate=50`

Sub-domain Enum
1. `ffuf -w SecLists/Discovery/DNS/subdomains-top1million-20000.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/' -H 'HOST: FUZZ.website.com' -fs 2309`
3. `python3 sublist3r -d <domain>`

Sub-Directoy Enum
1. `ffuf -w SecLists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u "http://<SERVER_IP>:<PORT>/FUZZ" -recursion -recursion-depth 1 -e .php`
2. `gobuster dir -x php,txt -u 10.129.255.70 -w /usr/share/wordlists/dirb/common.txt`

Parameter Fuzzing
1. `ffuf -w SecLists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=FUZZ' -fs 2287`
2. `ffuf -w SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://<SERVER_IP>:<PORT>/admin/admin.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx`

Page Type Fuzzing
1. `ffuf -w SecLists/Discovery/Web-Content/web-extensions.txt:FUZZ -u "http://<SERVER_IP>:<PORT>/indexFUZZ"`

SQLmap
- GET: `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php?id=1"`
- POST: `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --data "id=1"`
- Cookies: `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --cookie="id=1*"`
- JSON:  `Copy Request Headers --> req.txt; add in the JSON with "" surrounding the variables; sqlmap -r req.txt`


1. `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --data "id=1" --dbs`
2. `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --data "id=1" -D <database> --tables`
3. `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --data "id=1" -D <database> -T <table> --dump`
4. 3. `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --data "id=1" -D <database> -T <table> -C <column> --dump`

`--flush-session` to start again

`--no-cast` to ensure correct data is gotten from blind sql

`--risk=3` for more aggressive SQLi detection

Other stuff
- Check SSL cert
- Check email domains
- Check 404 pages
- Try both `/tmp` and `/dev/shm` for file writes
