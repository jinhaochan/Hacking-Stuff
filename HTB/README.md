# General Approach to HTB

1. `wfuzz -w SecLists/Discovery/DNS/subdomains-top1million-20000.txt -H "Host: FUZZ.<domain>"  -u 'http://<domain>' --hh <word size>`
2. `gobuster dir -u <addr> -w /usr/share/wordlist/dirb/common.txt`
3. `gobuster dir -x php,txt -u 10.129.255.70 -w /usr/share/wordlists/dirb/common.txt`
4. `nmap -sSV -Pn -p- -A <target>`
5. `nmap -sU -v <target> --min-rate=50`

Other stuff
- Check SSL cert
- Check email domains
- Check 404 pages
- Try both `/tmp` and `/dev/shm` for file writes
