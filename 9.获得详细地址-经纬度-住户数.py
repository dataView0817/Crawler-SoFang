# coding=utf-8
import requests
import codecs
from bs4 import BeautifulSoup
import re
import codecs
import os.path
import logging
'''
    获得可用的代理
'''
def getProxy():
    datas={
        'tid':'559464980977595',
        'num':1
        #'longlife':20
    }
    while True:
        url='http://vtp.daxiangdaili.com/ip'
        r = requests.get(url,params=datas)
        ips = r.text
        ips = ips.split('\r\n')
        ip = ips[0]
        print ip
        try:
            res = requests.get('http://www.baidu.com',timeout=10,proxies={'http':ip})
        except:
            continue
        else:
            return ip

def url_retry(url,num_retries=3):
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Cookie':'UM_distinctid=15d0cd2f4b57ea-061028fc77ccf9-871133d-100200-15d0cd2f4b6988; sale_rent_sb_298=eyJpdiI6Ilk1d1ZVNkhZZ2Z0OUIxUWtsRlIrSUE9PSIsInZhbHVlIjoieWpPd0dRQ1wvWnIxU0VEU2Uyd0d5WlE9PSIsIm1hYyI6IjFmYWVhNjUwNzE4MzYyY2E1ODNkNWExOTdiNDQzYzBkODI3MGZiOWQwZGQ1YTA4YTYxYzYxOGM0YThlZjM1ZTkifQ%3D%3D; sale_rent_sb_1=eyJpdiI6ImhobnJKNDdybzBPZmk4clwvMjlRQm1BPT0iLCJ2YWx1ZSI6InhwNEczUU01RUZuT1pUWlI1bUluTnc9PSIsIm1hYyI6IjUxZGRlZmEyMTZmNTkxZTJlZGFmYWUwMGIwMjc2NDk0OGI2MGM0N2NhMTQzZmM5MDBmNzUzNmZlNzkzN2QyZTcifQ%3D%3D; sale_rent_sb_17=eyJpdiI6IjBFQXg5MDdJREFLY2hQMnh6XC8zbVN3PT0iLCJ2YWx1ZSI6IlZHZmw2VEZybHFEMktSSW1Oa0Rub0E9PSIsIm1hYyI6IjhjMzU5NjA5ZjcxODFlMGEyNGM0YjU2ZTQ2ODk0MTBlYmE1NWE4NjhjMDhiODIzMzFiMjgwYmMwMDFkODZhNzgifQ%3D%3D; sale_rent_sb_340=eyJpdiI6IlFCQlFYbFVDVFpCc210T1FhVER5VkE9PSIsInZhbHVlIjoiQWFpWXlPM3pYeFMxZCt4NlwvMHBcL0xRPT0iLCJtYWMiOiI1YmU4MGQzZThiMmNiOGM2ZGIyYjUwODI5YTY2MTE1ZWY2MjgyZjJhNmY2YTUzYzQyMDIyYWZhNGU1NTZlNTEzIn0%3D; BDTUJIAID=142b1fcfda9738906f6b1986c2c688ca; sale_rent_sb_2=eyJpdiI6InVwV2srXC9KYW1SWXRpamhSdG9zNEx3PT0iLCJ2YWx1ZSI6IkJaRnVZa1dKMW5ld0o0b2dtZ2ZYK0E9PSIsIm1hYyI6IjJkYTVmZGFmNGVkYTRhMDFkYjYwYTQwNWQ4OTU3YzVlN2JkOWM4ZmZiZTZhZDBkMWUzMjUyZDgxM2NmYTFkZWQifQ%3D%3D; CNZZDATA1262285598=1862460761-1500720883-%7C1500720883; sale_rent_sb_20=eyJpdiI6IlRzRnRBaGdMVVZYS2Y3NEhjdGFRb3c9PSIsInZhbHVlIjoiMGE4SzlZc1wvV1M1bXgycTRnTDRyVVE9PSIsIm1hYyI6ImQxZTdjYmM5NTQ4ODg3YWQ5N2EwZGRiYzk5NWFlN2YyZGEzZWM2OTJlN2QxOGE3OTAzMWY3N2ZlMThjYTI1MjEifQ%3D%3D; cityid=eyJpdiI6IlE0OEpNeGhHcnFJWFZXYUQrOHNRbEE9PSIsInZhbHVlIjoiRk51K0VLdmh4MExCUU1ZRGxJbnhhUT09IiwibWFjIjoiMDEzZDFhMDIyMTJmOGVmMTcyM2I0ZDk5ZWI3MjAyNGJkN2JmMmI0MzMyMjkxNDI2MWRiN2NkNDA4YjIyM2QxMCJ9; city=eyJpdiI6IkRRMXY2NUJwaEQ3NFU3QzlUMmJ0VEE9PSIsInZhbHVlIjoiNGk4SGlxeWxXSHNaellISUthc3JXY0huS2RQaHBGc1JcL0dOSmdkN1FHU0lDVHV4K1hSb291WWxJZlJDK2luWSs3bmlWNytWXC9sXC8yTitKVWhRUk45ZnduYytYTVhGKzBHYUtGXC9mNll5bFo0aXpRMWs3V0Z1Y0VsOXBwalF5bk9JbHAzZDhnMk1kZ1NLcWtIVzhjTzhWdWZjQ01ZSWxOV1FZcHl5azR0MHN6XC9PcFdINVM1Rmt3XC9iZGJUdnJDK0xVNlg2VkFGWDVCd1hQUmQ3WU81QmlMZWh1RCtDK0lPTWtCdTZtQ3A0SldVUzVDMFwvTHdhc1BMcjl3N3NcL29ZZWxyOGhmK2l1N0lWaHRoU3d4S0FvOW9TS1B6bkY3ZFA1RnlJd2w4NnQwKzFKND0iLCJtYWMiOiI4OGY0NzZkODYwNjAwOWViMDgyMDRkYTBjYzQxMGViNmNhZWFmYjI0NTMxMjQxYmM5MjU3M2E4ZTMxY2FmZDU5In0%3D; citypy=eyJpdiI6InhrRHZ4Z0dtbXBtZzREaGR2REJmQlE9PSIsInZhbHVlIjoiRk55OTV4ZG9jdHkyVHpPNklDcXpaUT09IiwibWFjIjoiODQ3ZTMwOGE3YjRkMWMxOTFiOTE5MzM1ZGE5OWQ2ZTA5Y2RmMWU0MWI0YmE0NDUzOTcyM2ZjY2EyNzE2MWVhMSJ9; sale_rent_sb_28=eyJpdiI6Ijd1VXQ3MThWeldvRnI0VVAzckVoTFE9PSIsInZhbHVlIjoibGtwTWdqXC90YmJjWmZCbEFsZDVDb2c9PSIsIm1hYyI6IjE1OGZlYjU4NmI2NTMwYzE4N2ZiNTI3ZTA1ZWQyZDQzMDcwMzdkMjNlMDNkOTAzNjdhNGI3MGVjZWYxZWVlNTkifQ%3D%3D; Hm_lvt_d2801fc638056c1aac7e8008f41cf828=1499158738,1499175369; Hm_lpvt_d2801fc638056c1aac7e8008f41cf828=1500797004',
        'Host':'chizhou.sofang.com',
        'Pragma':'no-cache',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
    try:
        request=requests.get(url,headers = headers,timeout=10)
        #raise_for_status(),如果不是200会抛出HTTPError错误
        request.raise_for_status()
        html=request.text
        return html
    except requests.HTTPError as e:
        print "retrying..."
        html=None
        if num_retries>0:
            #如果不是200就重试，每次递减重试次数
            return url_retry(url,num_retries-1)
    #如果url不存在会抛出ConnectionError错误，这个情况不做重试
    except requests.exceptions.ConnectionError as e:
        return

        
        
'''
    line：代表要爬取的城市
'''
def getData(line,xqStart):
    line = line.strip('\r\n')
    shenName = line.split(u'^')[0]
    cityName = line.split(u'^')[2]
    print shenName,cityName,'begin'
    cityUrl = line.split(u'^')[3]
    f1 = codecs.open(u'F:\\sofang2\\5.'+shenName+u"_"+cityName+u'-小区名-对应url-价格.txt','r','utf-8')
    logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            filename=u'f:\\sofang2\\logging\\'+shenName+u"_"+cityName+u".log",
            filemode='a')
    lineslines = f1.readlines()
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

        html_cont = url_retry(xqUrl,10)
            
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
    if os.path.exists(path):#如果文件存在
        print shenName+u"_"+cityName+u" 已经存在"
        f2 = codecs.open(path,'r','utf-8')
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        f1.close()
        f2.close()
        if(len(lines1)==len(lines2)):
            print u"完全爬取",len(lines1),len(lines2)
        else:
            print u"爬取不完全",len(lines1),len(lines2)
            getData(line,len(lines2))
    else:#如果文件不存在
        lines1 = f1.readlines()
        f1.close()
        print shenName+u"_"+cityName+u" 还不存在 需要",len(lines1)
        getData(line,0)
    continue
