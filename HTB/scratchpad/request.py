import requests

url = "http://10.10.10.58:3000/api/session/authenticate?username=admin&password=password"

r = requests.post(url)

print(r.text)
