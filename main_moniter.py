import random
import requests
import re
import smtplib
import json
import re
from email.mime.text import MIMEText
from email.utils import formataddr
import sys
from http import cookiejar
import base64
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#关闭https认证警告
name=sys.argv[1] #sys.argv[1] 
sn=sys.argv[2] #sys.argv[2] 
idCard=sys.argv[3] #sys.argv[3] 
area=sys.argv[4] #sys.argv[4] '余区'
location = {
    '余区':'eyJlcXVpcG1lbnRzIjoiaVBob25lLWlQYWQtUHJvIiwiZGlhZ25vc2lzTmFtZSI6IiIsInJlbGF0aW9uV2l0aE93biI6IiIsImN1cnJlbnRBZGRyZXNzIjoi5rmW5YyX55yB5q2m5rGJ5biC5q2m5piM5Yy65Y+L6LCK5aSn6YGTNzEzLTHlj7ciLCJyZW1hcmsiOiIiLCJoZWFsdGhJbmZvIjoi5q2j5bi4IiwiaXNEaWFnbm9zaXMiOjAsImlzRmV2ZXIiOjAsImlzSW5TY2hvb2wiOjEsImlzTGVhdmVDaGVuZ2R1IjowLCJpc1N5bXB0b20iOiIwIiwidGVtcGVyYXR1cmUiOiIzNsKwQ+S7peS4iyIsInByb3ZpbmNlIjoi5rmW5YyX55yBIiwiY2l0eSI6IuatpuaxieW4giIsImNvdW50eSI6IuatpuaYjOWMuiJ9',
    '马区':'eyJlcXVpcG1lbnRzIjoiaVBob25lLWlQYWQtUHJvIiwiZGlhZ25vc2lzTmFtZSI6IiIsInJlbGF0aW9uV2l0aE93biI6IiIsImN1cnJlbnRBZGRyZXNzIjoi5rmW5YyX55yB5q2m5rGJ5biC5rSq5bGx5Yy654+e54uu6LevIiwicmVtYXJrIjoiIiwiaGVhbHRoSW5mbyI6Iuato+W4uCIsImlzRGlhZ25vc2lzIjowLCJpc0ZldmVyIjowLCJpc0luU2Nob29sIjoiMSIsImlzTGVhdmVDaGVuZ2R1IjowLCJpc1N5bXB0b20iOiIwIiwidGVtcGVyYXR1cmUiOiIzNlwiQ34zNi41wrBDIiwicHJvdmluY2UiOiLmuZbljJfnnIEiLCJjaXR5Ijoi5q2m5rGJ5biCIiwiY291bnR5Ijoi5rSq5bGx5Yy6In0=',
    "装杯":"eyJlcXVpcG1lbnRzIjoiaVBob25lLWlQYWQtUHJvIiwiZGlhZ25vc2lzTmFtZSI6IiIsInJlbGF0aW9uV2l0aE93biI6IiIsImN1cnJlbnRBZGRyZXNzIjoi5Yqgb3Blbklk6aqM6K+B5Lmf5aSq54ug5LqG5ZCn8J+Yre+8jOaIkeWQkeS9oOmBk+atie+8jOS4jeivpeivtOS9oOeahOe9kemhteWBmueahOS4jeWlvSIsInJlbWFyayI6IiIsImhlYWx0aEluZm8iOiLmraPluLgiLCJpc0RpYWdub3NpcyI6MCwiaXNGZXZlciI6MCwiaXNJblNjaG9vbCI6MSwiaXNMZWF2ZUNoZW5nZHUiOjAsImlzU3ltcHRvbSI6IjAiLCJ0ZW1wZXJhdHVyZSI6IjM2wrBD5Lul5LiLIiwicHJvdmluY2UiOiLmuZbljJfnnIEiLCJjaXR5Ijoi5q2m5rGJ5biCIiwiY291bnR5Ijoi5q2m5piM5Yy6In0="
}

def transformtobs64(text):
    a = str(base64.b64encode(text.encode('utf-8'))).split("'")[1]


    return a

Header = {
        'Host':"zhxg.whut.edu.cn",
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'X-Tag':'flyio',
        'content-type':'application/json',
        'Accept-Encoding':'gzip,br,deflate',
        'encode':"true",
        'Content-Length': '136',
        'Referer':'https://servicewechat.com/wxa0738e54aae84423/21/page-frame.html',
}
url='https://zhxg.whut.edu.cn/yqtjwx/'
myflag = False
bind = True
def transform2(res):
    a = json.loads(res)['data']
    b = list(str(base64.b64decode(a)))
    c = []
    str1 = ''
    for i in range(2,len(b)-1):
        c.append(b[i])
    for i in c:
        str1 += i

    bind = json.loads(str1.replace('\\', '\\\\'),strict=False)['bind']
    return bind
while myflag ==False or bind == True:
    openid = '0610qm100dFVBN1DFS300PFKd830'+random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')+random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')+random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')+random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    check_data = transformtobs64('{"openid":"'+openid+'","sn":null,"idCard":null,"avatarurl":null,"nickname":null}')
    session = requests.session()
    check = session.post(url + "api/login/checkBind", data=check_data, headers=Header, verify=False)
    myflag = json.loads(check.text)['status']
    bind = transform2(check.text)

#固定数据，就不用转换浪费内存了
#后续修正，openid使用随机数字监控bind是否为false再下一步



def transform(res):
    a = json.loads(res)['data']
    b = list(str(base64.b64decode(a)))
    c = []
    str1 = ''
    for i in range(2,len(b)-1):
        c.append(b[i])
    for i in c:
        str1 += i

    dic_cookies = 'JSSESSION='+json.loads(str1.replace('\\', '\\\\'),strict=False)['sessionId']
    return dic_cookies


#转换base64函数
dic_cookies = transform(check.text)

Header['Cookie']=dic_cookies
#'{"sn":"0122018390620","idCard":"18003X","avatarurl":"","nickname":"微信用户"}'
bind_data = transformtobs64('{"sn":"'+sn+'","idCard":"'+idCard+'","avatarurl":"","nickname":"微信用户"}')
myflag = False
while(myflag==False):
    bindUserInfo = requests.post(url+'api/login/bindUserInfo', data=bind_data, headers=Header,verify=False)
    myflag = json.loads(bindUserInfo.text.replace('\\', '\\\\'), strict=False)['status']
    message = json.loads(bindUserInfo.text.replace('\\', '\\\\'), strict=False)['message']
    if message == '该学号已被其它微信绑定':
        break

    elif (message == '输入信息不符合'):
        break
    elif (message == '身份证信息错误'):
        break
    else:
        continue
def transform1(res):
    a = json.loads(res)['data']
    b = list(str(base64.b64decode(a)))
    c = []
    str1 = ''
    for i in range(2,len(b)-1):
        c.append(b[i])
    for i in c:
        str1 += i

    str1 = json.loads(str1.replace('\\', '\\\\'), strict=False)['user']['name']
    return str1

message = json.loads(bindUserInfo.text.replace('\\', '\\\\'),strict=False)['message']

if message =='该学号已被其它微信绑定':
    print("code1")

elif(message =='输入信息不符合'):
    print('code2')
elif(message == '身份证信息错误'):
    print('code3')
else:
    P=transform1(bindUserInfo.text)
    s = eval(repr(P).replace("\\\\", "\\"))
    s=s.encode('raw_unicode_escape').decode()
    print('code4\n')




location_data =location[area]


monitorRegister = requests.post(url+'monitorRegister',data=location_data,headers=Header,verify=False)

cancelBind = requests.post(url+'api/login/cancelBind', data=json.dumps({}), headers=Header,verify=False)

