#!/usr/bin/env python
# -*- coding: utf-8-*-

import time
import urllib2
from bs4 import BeautifulSoup
import sqlite3
import json




website = 'http://www.qianlima.com/zb/area_1049_0_1'


class logClass():
    id = 0
    title = ''
    date = ''
    read = ''


def getdate():
    return time.strftime("%Y-%m-%d-%H:%M", time.localtime())


def getmailtitle():
    return '招标信息' + getdate()


def getmailstring():
    request = urllib2.Request(website)
    request.add_header("User-Agent",
                       "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6")
    response = urllib2.urlopen(request)
    htmlstring = response.read()
    htmlstring = unicode(htmlstring,'gbk')
    response.close()
    html =BeautifulSoup(htmlstring, 'html.parser')
    firt_record = html.findAll('td', attrs={'width': '85%', 'align': 'left'}, limit=30)
    second_record = html.findAll('td', attrs={'width': '12%', 'align': 'left'}, limit=30)

    list = []

    for i in range(0, firt_record.__len__()):
        f = firt_record[i].get_text()
        s = second_record[i].get_text()
        string = f + '-' + s
        list.append(string)

    mailstring = ''

    for i in list:
        mailstring = mailstring + i + "\n"
    mailstring = mailstring + getdate()

    return mailstring

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '36516839@qq.com'  # 设置发件邮箱
my_pass = 'lshtywmymwtscaig'  # 设置发件邮箱密码
my_users = ['36516839@qq.com', '1125871486@qq.com', '37984544@qq.com']#收件人列表


def mail(sendto):
    ret = True
    try:
        # 邮件标题
        mailtitle = getmailtitle()
        # 邮件内容
        mailcontent = getmailstring()

        msg = MIMEText(mailcontent, 'plain', 'utf-8')
        msg['From'] = formataddr(["From", my_sender])  # 发件人
        msg['To'] = formataddr(["FK", sendto])  # 收件人
        msg['Subject'] = mailtitle  # 主题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 设置smtp服务器
        server.login(my_sender, my_pass)  # 登录服务器
        server.sendmail(my_sender, [sendto, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 失败返回ret=False
        ret = False
    return ret


def sendmail():
    for i in my_users:
        ret = mail(i)
        if ret:
            print("mail send to " + i + " success")
        else:
            print("mail send to " + i + " failed")


def printmail():
    print getmailstring()

if __name__ == "__main__":
    sendmail()

    # printmail()