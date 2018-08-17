# coding=utf-8
from lib import HtmlDownloader
from bs4 import BeautifulSoup
import re
import codecs
f = codecs.open(u'F:\\sofang2\\1.所有城市（带所属省份）.txt','w','utf-8')
url = u"http://cs.sofang.com/city/citysList"

html_cont = HtmlDownloader.download(url)
while html_cont is None:
    print "retrying..."+url
    html_cont = HtmlDownloader.download(url)
html_cont = unicode(html_cont,'utf-8')
soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
citys = soup.find('div',class_='citylist').find_all("div")[1].find_all('ul')[0].find_all('li')
L = []
for city in citys:
    if city.find('label').text.strip()!="" :
        shenName = city.find('label').text.strip()
    cityCityS = city.find('p').find_all('a')
    for cityCity in cityCityS:
        cityName = cityCity.text
        cityUrl = cityCity[u'href']
        #print shenName,cityName,cityUrl
        f.write(shenName+u"^"+cityName+u"^"+cityUrl+u"\r\n")

