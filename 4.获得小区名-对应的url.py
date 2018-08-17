# coding=utf-8
from lib import HtmlDownloader
from bs4 import BeautifulSoup
import re
import codecs
f = codecs.open(u"F:\\sofang2\\2.省_城市_对应URL.txt",'r','utf-8')
lines = f.readlines()
#对每一个city 每一个city整理一个文件
for line in lines[200::1]:
    line = line.strip('\r\n')
    shenName = line.split(u'^')[0]
    cityName = line.split(u'^')[2]
    cityUrl = line.split(u'^')[3]
    f1 = codecs.open(u"F:\\sofang2\\3."+shenName+u"_"+cityName+u"-区-对应url.txt",'r','utf-8')
    f2 = codecs.open(u'F:\\sofang2\\4.'+shenName+u"_"+cityName+u'-小区名-对应url-价格.txt','w','utf-8')
    lineslines = f1.readlines()
    #对每一个area
    for lineline in lineslines:
        lineline = lineline.strip()
        areaName = lineline.split('^')[2]
        areaUrl = lineline.split('^')[4]
        print shenName,cityName,areaName,areaUrl
        url =  areaUrl+u'-bl1'
        #对每一页
        while True:
            html_cont = HtmlDownloader.download(url)
            while html_cont is None:
                print "retrying..."+url
                html_cont = HtmlDownloader.download(url)
            soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
            list_list_free = soup.find(text=u'全部小区').parent.parent.parent.parent
            try:
                xqs = list_list_free.find('div',class_='list list_free').find_all('dl')
            except:#一页数据也没有
                break
            for xq in xqs:
                house_msg = xq.find("dd",class_='house_msg')
                xqName = house_msg.p.a.text
                xqUrl = cityUrl+house_msg.p.a[u'href']
                house_price = xq.find("dd",class_='house_price')
                xqPrice = house_price.p.text
                xqPrice = re.sub('\D','',xqPrice)
                f2.write(xqName+u","+shenName+u","+cityName+u","+areaName+u","+xqPrice+u","+xqUrl+u","+areaUrl+u'\r\n')
            nextUrl = soup.find('a',text=u'下一页')
            if nextUrl is None:
                break
            else:
                url = cityUrl+nextUrl[u'href']