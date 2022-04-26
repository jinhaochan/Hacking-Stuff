# General Approach to HTB

1. `wfuzz -w SecLists/Discovery/DNS/subdomains-top1million-20000.txt -H "Host: FUZZ.<domain>"  -u 'http://<domain>' --hh <word size>`
2. `ffuf -w /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u 'http://1.1.1.1:2222/' -H 'HOST: FUZZ.website.com' -fs 2309`
3. `ffuf -w /opt/useful/SecLists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=FUZZ' -fs 2287`
4. `gobuster dir -u <addr> -w /usr/share/wordlist/dirb/common.txt`
5. `gobuster dir -x php,txt -u 10.129.255.70 -w /usr/share/wordlists/dirb/common.txt`
6. `nmap -sSV -Pn -p- -A <target>`
7. `nmap -sU -v <target> --min-rate=50`

Other stuff
- Check SSL cert
- Check email domains
- Check 404 pages
- Try both `/tmp` and `/dev/shm` for file writes
