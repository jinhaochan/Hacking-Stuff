# General Approach to HTB

nmap
1. `nmap -sSV -Pn -p- -A <target>`
2. `nmap -sU -v <target> --min-rate=50`

Sub-domain Enum
1. `wfuzz -w SecLists/Discovery/DNS/subdomains-top1million-20000.txt -H "Host: FUZZ.<domain>"  -u 'http://<domain>' --hh <word size>`
2. `ffuf -w SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u 'http://1.1.1.1:2222/' -H 'HOST: FUZZ.website.com' -fs 2309`
3. `python3 sublist3r -d <domain>`

Sub-Directoy Enum
1. `ffuf -w ~/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u "http://167.71.139.140:31516/FUZZ" -recursion -recursion-depth 1 -e .php`
2. `gobuster dir -x php,txt -u 10.129.255.70 -w /usr/share/wordlists/dirb/common.txt`

Parameter Fuzzing
1. `ffuf -w /opt/useful/SecLists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=FUZZ' -fs 2287`


Other stuff
- Check SSL cert
- Check email domains
- Check 404 pages
- Try both `/tmp` and `/dev/shm` for file writes
