#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import urllib2
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding( "utf-8" )

toupwebsite = 'http://www.yixf.net/plugin.php?id=hejin_toupiao&model=top300&vid=4#top300'

# 逐条处理读取并返回一条信息
def writetoupiaolog():
    response = urllib2.urlopen(toupwebsite)
    htmlstring = response.read()
    response.close()

    #去除html标记
    html = BeautifulSoup(htmlstring, 'html.parser')

    # 遍历
    result_Record = html.findAll('li', attrs={'class': 'list'}, limit=5)
    i = 0
    xstring = ''
    while i < 5:
        result_Table=result_Record[i].findAll('span')
        i = i + 1
        j = 0
        while j <4:
            xstring = xstring + result_Table[j].get_text().rjust(15)
            j =j +1
        xstring = xstring + '\n'

    writelog(xstring)


#写文件函数
def writelog(logtxt):
    f = open('logo.txt','a')
    f.write(logtxt)
    f.flush()
    f.close()

#时间戳函数
def timer(n):
    conuter = 1
    while True:
        timenow = time.strftime('%Y-%m-%d %X', time.localtime())
        countrecord = '#log#%05d'%conuter +'#'+timenow+'\n'
        print '*'*6, '#log#%05d'%conuter+'#'+timenow, '*'*6
        writelog(countrecord)
        try:
            writetoupiaolog()
        except:
            print '加载出错'
            writelog('加载出错\n')
        conuter = conuter + 1
        time.sleep(n)

if __name__ == '__main__':
    timer(600)