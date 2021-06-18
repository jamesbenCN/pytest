# -*- coding: utf-8-*-

import urllib2
import re

# webSites = {
#     # 采集页面网址
#     'name': u'竹溪县',
#     'url': 'http://www.zhuxi.gov.cn/zwxx/xxgkml/zbcg_9016/list_226.shtml',
#     'linkRule': 'http://www.zhuxi.gov.cn/zwxx/xxgkml/zbcg_9016/',
#     # 模块采集正则表达式
#     'blockRes': r'(<td onmouseover="displayTip[\S\s]+?</p>[\s]+)',
#     'titleRes': r'<a .*?>(.*?)</a>',
#     'linkRes': r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')',
#     'dateRes': r'/t(.*?)_',
#     'keyRes': r'/t.*?_(.*?).shtml'
# }

# webSites = {
#     # 采集页面网址
#     'name': u'竹山县',
#     'url': 'http://www.zhushan.gov.cn/zwgk/zl/xxgkml/zbtb/list_2233.shtml',
#     'linkRule': 'http://www.zhushan.gov.cn/zwgk/zl/xxgkml/zbtb/zbgs_26946/',
#     # 模块采集正则表达式
#     'blockRes': r'(<td onmouseover="displayTip[\S\s]+?</p>[\s]+)',
#     'titleRes': r'<a .*?>(.*?)</a>',
#     'linkRes': r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')',
#     'keyRes': r'/t.*?_(.*?).shtml',
#     'dateRes': r'/t(.*?)_',
# }
#
# webSites = {
#     # 采集页面网址
#     'name': u'房县',
#     'url': 'http://www.cnfx.gov.cn/zwgk_t/xxgkzl/xxgkml_31749/zfcg_34090/list_2956.shtml',
#     'linkRule': 'http://www.cnfx.gov.cn/zwgk_t/xxgkzl/xxgkml_31749/ggzy/',
#     # 模块采集正则表达式
#     'blockRes': r'(<td onmouseover="displayTip[\S\s]+?</p>[\s]+)',
#     'titleRes': r'<a .*?>(.*?)</a>',
#     'linkRes': r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')',
#     'keyRes': r'/t.*?_(.*?).shtml',
#     'dateRes': r'/t(.*?)_',
# }

# webSites = {
#     # 采集页面网址
#     'name': u'丹江口市',
#     'url': 'http://www.djk.gov.cn/zwgk/xxgkzl/xxgkml/zbcg/list_3978.shtml',
#     'linkRule': 'http://www.djk.gov.cn/zwgk/xxgkzl/xxgkml/zbcg/cjjg/',
#     # 模块采集正则表达式
#     'blockRes': r'(<td onmouseover="displayTip[\S\s]+?</p>[\s]+)',
#     'titleRes': r'<a .*?>(.*?)</a>',
#     'linkRes': r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')',
#     'keyRes': r'/t.*?_(.*?).shtml',
#     'dateRes': r'/t(.*?)_',
# }

# webSites = {
#     # 采集页面网址
#     'name': u'郧西县',
#     'url': 'http://www.yunxi.gov.cn/zwgk/xxgkzl/xxgkml/zfcg/list_4002.shtml',
#     'linkRule': 'http://www.yunxi.gov.cn/zwgk/xxgkzl/xxgkml/zfcg/zbcjjg/',
#     # 模块采集正则表达式
#     'blockRes': r'(<td onmouseover="displayTip[\S\s]+?</p>[\s]+)',
#     'titleRes': r'<a .*?>(.*?)</a>',
#     'linkRes': r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')',
#     'keyRes': r'/t.*?_(.*?).shtml',
#     'dateRes': r'/t(.*?)_',
# }

# webSites = {
#     # 采集页面网址
#     'name': u'郧阳区',
#     'url': 'http://www.hbyx.gov.cn/xxgk/zfxxgkzl/zfxxgkml/zfcg/list_4504.shtml',
#     'linkRule': 'http://www.hbyx.gov.cn/xwzx/gsgg/',
#     # 模块采集正则表达式
#     'blockRes': r'(<td onmouseover="displayTip[\S\s]+?</p>[\s]+)',
#     'titleRes': r'<a .*?>(.*?)</a>',
#     'linkRes': r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')',
#     'keyRes': r'/t.*?_(.*?).shtml',
#     'dateRes': r'/t(.*?)_',
# }

webSites = {
    # 采集页面网址
    'name': u'张湾区',
    'url': 'http://www.zhangwan.gov.cn/zwgk/xxgkzl/xxgkml/tbzb/list_1305.shtml',
    'linkRule': 'http://www.zhangwan.gov.cn/zwgk/xxgkzl/xxgkml/tbzb/',
    # 模块采集正则表达式
    'blockRes': r'(<td onmouseover="displayTip[\S\s]+?</p>[\s]+)',
    'titleRes': r'<a .*?>(.*?)</a>',
    'linkRes': r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')',
    'keyRes': r'/t.*?_(.*?).shtml',
    'dateRes': r'/t(.*?)_',
}
#
# webSites = {
#     # 采集页面网址
#     'name': u'茅箭区',
#     'url': 'http://maojian.shiyan.gov.cn/zwgk/zl/xxgkml/zfcg/list_1488.shtml',
#     'linkRule': 'http://maojian.shiyan.gov.cn/zwgk/zl/xxgkml/zfcg/',
#     # 模块采集正则表达式
#     'blockRes': r'(<td onmouseover="displayTip[\S\s]+?</p>[\s]+)',
#     'titleRes': r'<a .*?>(.*?)</a>',
#     'linkRes': r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')',
#     'keyRes': r'/t.*?_(.*?).shtml',
#     'dateRes': r'/t(.*?)_',
# }

# webSites = {
#     # 采集页面网址
#     'name': u'白浪经济开发区',
#     'url': 'http://www.sygxq.gov.cn/zwgk/xxgkzl/xxgkml/zbcg/list_3047.shtml',
#     'linkRule': 'http://www.sygxq.gov.cn/zwgk/xxgkzl/xxgkml/zbcg/',
#     # 模块采集正则表达式
#     'blockRes': r'(<td onmouseover="displayTip[\S\s]+?</p>[\s]+)',
#     'titleRes': r'<a .*?>(.*?)</a>',
#     'linkRes': r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')',
#     'keyRes': r'/t.*?_(.*?).shtml',
#     'dateRes': r'/t(.*?)_',
# }

# webSites = {
#     # 采集页面网址
#     'name': u'武当山特区',
#     'url': 'http://zw.wudangshan.gov.cn/zwgk_30286/xxgkml/zbcg/list_3041.shtml',
#     'linkRule': 'http://zw.wudangshan.gov.cn/zwgk_30286/xxgkml/zbcg/',
#     # 模块采集正则表达式
#     'blockRes': r'(<td onmouseover="displayTip[\S\s]+?</p>[\s]+)',
#     'titleRes': r'<a .*?>(.*?)</a>',
#     'linkRes': r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')',
#     'keyRes': r'/t.*?_(.*?).shtml',
#     'dateRes': r'/t(.*?)_',
# }

# webSites = {
#     # 采集页面网址
#     'name': u'十堰市政府',
#     'url': 'http://www.shiyan.gov.cn/sysgovinfo/szf/xxgkml/zbcg/list_50.shtml',
#     'linkRule': 'http://www.shiyan.gov.cn/sysgovinfo/szf/xxgkml/zbcg/',
#     # 模块采集正则表达式
#     'blockRes': r'(<td onmouseover="displayTip[\S\s]+?</p>[\s]+)',
#     'titleRes': r'<a .*?>(.*?)</a>',
#     'linkRes': r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')',
#     'keyRes': r'/t.*?_(.*?).shtml',
#     'dateRes': r'/t(.*?)_',
# }


class Spider:
    # 爬取网页的地址
    url = ""
    linkRule = ""
    blockRes = ""

    defaultTitleRes = r'<a .*?>(.*?)</a>'
    defaultLinkRes = r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')'
    defaultDateRes = r'/t(.*?)_'
    defaultKeyRes = r'/t.*?_(.*?).shtml'

    webName = ""
    moduleName = ""

    def getHtml(self):
        url = self.url
        request = urllib2.Request(url)
        request.add_header("User-Agent",
                           "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6")
        response = urllib2.urlopen(request)
        htmlstring = response.read()
        response.close()
        return htmlstring

    # 获取网页中信息块
    def getBlock(self):
        html = self.getHtml()
        block = re.findall(self.blockRes, html)
        return block

    # 获取单条信息标题
    def getTitle(self, item, res=defaultTitleRes):
        titles = re.findall(res, item, re.S | re.M)
        for title in titles:
            return title

    # 获取单条信息链接
    def getLink(self, item, res=defaultLinkRes):
        urllist = self.url.rsplit('/', 1)
        url =urllist[0]
        links = re.findall(res, item, re.I | re.S | re.M)
        for link in links:
            pass
            # if '../../' in link
            # link = link
            # return url+link



    # 获取发文日期
    def getDate(self, item, res=defaultDateRes):
        dates = re.findall(res, item, re.S | re.M)
        for date in dates:
            return date

    # 获取文章键值
    def getKey(self, item, res=defaultKeyRes):
        keys = re.findall(res, item, re.S | re.M)
        for key in keys:
            return key

    def getContent(self):
        pass

    # 打印爬取的信息含标题和网址
    def printtitlelink(self):
        block = self.getBlock()
        for item in block:
            title = self.getTitle(item)
            link = self.getLink(item)
            date = self.getDate(link)
            key = self.getKey(link)
            print '['+date+'] ' + '=' + key + '=' + title + ' ' + link

if __name__ == "__main__":
        spider = Spider()
        spider.url = webSites['url']
        # spider.blockRes = webSites['blockRes']
        # spider.linkRule = webSites['linkRule']
        # spider.printtitlelink()
        spider.getLink()



