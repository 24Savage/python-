import requests
import json
import base64

# 发送请求至少需要一个url参数，此外还可能需要params(url参数,字典格式) data(请求数据,字典或字符串格式) headers, cookie, files, auth, timeout
url_for_token = 'https://aip.baidubce.com/oauth/2.0/token'
param = {'grant_type':'client_credentials',
        'client_id':'Lo57Xo4hr8q3TXKGDT3C0lwF',
        'client_secret':'lY7gtuKF5zxp4gdEzqiTibovjLbm4HsA'}
res = requests.get(url=url_for_token,params=param)
token = res.json()['access_token']

url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
header = {'content-type':'application/x-www-form-urlencoded'}
img = open(r'C:\Users\jiao\Pictures\2019-08\IMG_1683.JPG','rb')
data = {'image':base64.b64encode(img.read())}
res = requests.post(url=url, params={"access_token":token}, headers=header, data=data)
if res:
    print(res.json())