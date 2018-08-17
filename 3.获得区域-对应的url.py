# coding=utf-8
from lib import HtmlDownloader
from bs4 import BeautifulSoup
import re
import codecs

f1 = codecs.open(u"F:\\sofang2\\2.省_城市_对应URL.txt",'r','utf-8')
lines = f1.readlines()
for line in lines:
    line = line.strip('\r\n')
    shenName = line.split('^')[0]
    cityName = line.split('^')[2]
    f = codecs.open(u'F:\\sofang2\\3.'+shenName+u"_"+cityName+u"-区-对应url.txt",'w','utf-8')
    cityUrl = line.split('^')[3]
    print shenName,cityName,cityUrl
    url = cityUrl+u"/saleesb/area"
    html_cont = HtmlDownloader.download(url)
    while html_cont is None:
        print "retrying..."+url
        html_cont = HtmlDownloader.download(url)
    html_cont = unicode(html_cont,'utf-8')
    soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
    areas = soup.find('div',class_='search_info').parent.find('dd')
    areas = areas.find_all('a')
    for area in areas:
        areaName = area.text
        areaUrl = area[u'href']
        areaUrl = cityUrl + areaUrl
        if areaName.find(u"不限")==-1:
            f.write(shenName+u"^"+cityName+u"^"+areaName+u"^"+cityUrl+u"^"+areaUrl+u'\r\n')