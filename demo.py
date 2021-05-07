#!/usr/bin/env python
# -*- coding:utf-8 -*-
#import library
import schedule
import time
import itchat
import datetime
#login web wechat
itchat.auto_login(hotReload=True)
#search chatroom
user = itchat.search_chatrooms(name=u"office测试组")
#find self name
userName = user[0][u'UserName']


#def job
def job():
    for i in range(0, 3):
        itchat.send("打卡", toUserName=userName)
        time.sleep(1)
schedule.every().day.at("08:20").do(job)
schedule.every().day.at("17:35").do(job)
#rerun
while True:
    schedule.run_pending()
    # print current time
    now = datetime.datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')[11:]
    print('\r{}'.format(now_str), end='')