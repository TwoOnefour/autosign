from crontab import CronTab
import random
import sys
from moniter_data import *
import pymysql

conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '',
    db='mydb2')
cur = conn.cursor()

my_user_cron = CronTab(user='admin')
cur.execute('select * from information')
result = cur.fetchall()
print(result)
for i in range(result.__len__()):
    sn=result[i][0]
    idCard=result[i][1]
    name=result[i][2]
    area=result[i][3]
    minute = result[i][4].split(':')[1]
    hour = result[i][4].split(':')[0]
#处理数据
    my_user_cron.new(command='python3 /root/auto/main_moniter.py {0}{1}{2} {3}{4}{5} {6}{7}{8} {9}{10}{11}'.format('"',sn,'"','"',idCard,'"','"',name,'"','"',area,'"')).setall("{0}".format(minute)+' {0} * * *'.format(hour))
my_user_cron.write()
