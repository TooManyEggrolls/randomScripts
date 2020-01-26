import requests
import os
import random
import string
import json
import secrets

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

#Open Developer Tools in Chrome, check Preservce Log, capture Request URL
url = 'http://craigslist.pottsfam.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhasdasd2.php'
domains = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@aol.com', '@hotmail.com.uk', '@comcast.net', '@outlook.com', '@verizon.net']

names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))
	domains_extra = ''.join(random.choice(domains))

	username = name.lower() + name_extra + domains_extra
	##username = name.lower() + name_extra + '@yahoo.com'
	password = ''.join(secrets.choice(chars) for i in range(10))

	requests.post(url, allow_redirects=False, data={
    #Capture below Form Details from Developer Tools
		'auid2yjauysd2uasdasdasd': username,
		'kjauysd6sAJSDhyui2yasd': password
	})

	print(f"Sending username as {username} and Password as {password}")
    #print 'sending username %s and password %s' % (username, password)

	#Regix Search Replace list names, add quotes and comma, names.json
    #^([A-Za-Z]+1)$
    #"$1",
