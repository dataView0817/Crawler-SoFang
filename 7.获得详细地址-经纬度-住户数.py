# coding=utf-8
import requests
import codecs
from bs4 import BeautifulSoup
import re
import codecs
import logging

def getData(citys,xqStart):
    #对每一个city
    for line in citys:
        line = line.strip('\r\n')
        shenName = line.split(u'^')[0]
        cityName = line.split(u'^')[2]
        print shenName,cityName,'begin'
        if cityName==u'天津':
            continue
        cityUrl = line.split(u'^')[3]
        f1 = codecs.open(u'F:\\sofang2\\5.'+shenName+u"_"+cityName+u'-小区名-对应url-价格.txt','r','utf-8')
        
        logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=u'f:\\sofang2\\logging\\'+shenName+u"_"+cityName+u".log",
                filemode='w')
        
        
        lineslines = f1.readlines()
        if len(lineslines)>1000:
            continue
            
        f2 = codecs.open(u"F:\\sofang2\\6."+shenName+u"_"+cityName+u"-小区名-对应url-价格-经纬度-住户数.txt",'a','utf-8')
        #对每一个小区
        res = []
        for lineline in lineslines[xqStart::1]:
            lineline = lineline.strip('\r\n')
            xqName = lineline.split(',')[0]
            areaName = lineline.split(',')[3]
            xqPrice = lineline.split(',')[4]
            xqUrl = lineline.split(',')[5]
            areaUrl = lineline.split(',')[6]
            #print type(shenName),type(cityName),type(areaName),type(xqName),type(xqUrl)
            try:
                sss = shenName+" "+cityName+" "+areaName+" "+xqName+" "+xqUrl
                #print sss,type(sss)
                #logging.debug(xqName)
                pass
                #print shenName,cityName,areaName,xqName,xqUrl
            except:
                pass
            headers = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
     
            r = requests.get(xqUrl,headers=headers)
            html_cont = r.text
            while html_cont is None:
                print "retrying..."+url
                r = requests.get(xqUrl,headers=headers)
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
            res.append(xqName+u"^"+shenName+u"^"+cityName+u"^"+areaName+u"^"+xqAddr+u"^"+u"["+longitude+u","+latitude+u"]"+u"^"+zongHuShu+u"^"+xqPrice+"^"+xqUrl+u"^"+areaUrl+u"\r\n")
            if len(res)>100:
                for resres in res:
                    f2.write(resres)
                res=[]
        for resres in res:
            f2.write(resres)
        print shenName,cityName,'end'    



import time
from threading import Thread

class MyThread(Thread):
    def __init__(self, citys,xqStart):
        Thread.__init__(self)
        self.citys = citys
        self.xqStart = xqStart
        
    def run(self):
        print 'running'
        self.result = getData(self.citys,self.xqStart)
        
if __name__ == "__main__":


    f = codecs.open(u"F:\\sofang2\\2.省_城市_对应URL.txt",'r','utf-8')
    lines = f.readlines()
    thd1 = MyThread(lines[37:50:1],0)
    thd2 = MyThread(lines[50:70:1],0)
    thd3 = MyThread(lines[70:100:1],0)
    #thd4 = MyThread(5)
    thd1.start()
    thd2.start()
    thd3.start()
    thd1.join()
    thd2.join()
    thd3.join()
