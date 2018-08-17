# coding=utf-8
from lib import HtmlDownloader
from bs4 import BeautifulSoup
import re
import codecs
f1 = codecs.open(u'F:\\sofang2\\1.所有城市1.txt','w','utf-8')
f2 = codecs.open(u'F:\\sofang2\\1.所有城市2.txt','w','utf-8')
url = u"http://cs.sofang.com/city/citysList"

html_cont = HtmlDownloader.download(url)
while html_cont is None:
    print "retrying..."+url
    html_cont = HtmlDownloader.download(url)
html_cont = unicode(html_cont,'utf-8')
soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
citys = soup.find('div',class_='citylist').find("div",class_='citys')
citys1 = citys.find_all('ul')[0].find_all('a',href=re.compile('http:.*sofang.com'))
citys2 = citys.find_all('ul')[1].find_all('a',href=re.compile('http:.*sofang.com'))

print len(citys),len(citys1),len(citys2)
for city in citys1:
    cityName = city.text
    cityUrl = city[u'href']
    f1.write(cityName+u"^"+cityUrl+u"\r\n")

for city in citys2:
    cityName = city.text
    cityUrl = city[u'href']
    f2.write(cityName+u"^"+cityUrl+u"\r\n")
    
f1.close()
f2.close()