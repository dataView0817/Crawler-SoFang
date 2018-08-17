# coding=utf-8
import requests
import codecs
from bs4 import BeautifulSoup
import re
import codecs
import os.path

f = codecs.open(u"F:\\sofang2\\2.省_城市_对应URL.txt",'r','utf-8')
lines = f.readlines()
#对每一个city
for line in lines[303:304:1]:
    line = line.strip('\r\n')
    shenName = line.split(u'^')[0]
    cityName = line.split(u'^')[2]
    if cityName==u'天津':
        continue
    cityUrl = line.split(u'^')[3]
    f1 = codecs.open(u'F:\\sofang2\\5.'+shenName+u"_"+cityName+u'-小区名-对应url-价格.txt','r','utf-8')
    path = u"F:\\sofang2\\6."+shenName+u"_"+cityName+u"-小区名-对应url-价格-经纬度-住户数.txt"
    if os.path.exists(path):
        print shenName+u"_"+cityName+u" 已经存在"
        f2 = codecs.open(path,'r','utf-8')
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        if(len(lines1)==len(lines2)):
            print u"完全爬取",len(lines1),len(lines2)
        else:
            print u"爬取不完全",len(lines1),len(lines2)
    else:
        print shenName+u"_"+cityName+u" 还不存在"
    continue
    lineslines = f1.readlines()
    
    #对每一个小区
    for lineline in lineslines[0::1]:
        lineline = lineline.strip('\r\n')
        xqName = lineline.split(',')[0]
        areaName = lineline.split(',')[3]
        xqPrice = lineline.split(',')[4]
        xqUrl = lineline.split(',')[5]
        areaUrl = lineline.split(',')[6]
        try:
            print shenName,cityName,areaName,xqName,xqUrl
        except:
            pass
        headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
 
        r = requests.get(xqUrl,headers=headers,timeout = 10)
        html_cont = r.text
        while html_cont is None:
            print "retrying..."+url
            r = requests.get(xqUrl,headers=headers,timeout = 10)
            html_cont = r.text
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        zongHuShu = soup.find(text=re.compile(u'.*总户数.*')).parent.parent
        zongHuShu = zongHuShu.span.text.strip()
        zongHuShu = re.sub('\D','',zongHuShu)
        xqAddr = soup.find(text=re.compile(u'.*小区地址.*')).parent.parent
        xqAddr = xqAddr.h3.text.strip()
        longitude_latitude = soup.find('script',text=re.compile(r'.*var longitude.*'))
        longitude_latitude = longitude_latitude.text
        longitude_latitude = longitude_latitude[longitude_latitude.find('var longitude = "'):longitude_latitude.find('if((longitude == 0'):1]
        longitude = longitude_latitude.split('\"')[1]
        latitude = longitude_latitude.split('\"')[3]
        f2.write(xqName+u"^"+shenName+u"^"+cityName+u"^"+areaName+u"^"+xqAddr+u"^"+u"["+longitude+u","+latitude+u"]"+u"^"+zongHuShu+u"^"+xqPrice+"^"+xqUrl+u"^"+areaUrl+u"\r\n")