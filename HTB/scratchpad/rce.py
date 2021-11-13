import requests


url = "\
        http://forge.htb/uploads/6l4SzA9fVwfeKk2R9JUa"

r = requests.get(url)

print(r.text)
