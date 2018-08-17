# coding=utf-8
import HtmlDownloader
import urllib2
import JsonUtils
import json
'''
查询地理位置
    place:要查询的地理位置
    city:所在的城市
返回值：
    d 是一个dict
'''
def getPos(place,city):
    ak = u'BjZFyCBFktfZmdj7SVP98fEFx78KzFn4'
    #ak=u'skS8wg9wP1VVFk2iuDuQATzoWKMb8FuY'
    #ak=u'AKsr88dgGDK8d74q7wTRbhiSb567HVmA'
    d={}
    place=urllib2.quote(place)
    city=urllib2.quote(city)
    hd = HtmlDownloader.HtmlDownloader()
    ju =  JsonUtils.JsonUtils()
    url =u'http://api.map.baidu.com/geocoder/v2/?address=%s&output=json&ak=%s&city=%s' %(place,ak,city)
    print url
    res = hd.download(url)
    res = unicode(res,'utf-8')
    data = ju.readStr(res)

    status = data[u'status']
    if status==0:
        lng = data[u'result'][u'location'][u'lng']
        lat = data[u'result'][u'location'][u'lat']
        d[u"lng"]=unicode(str(lng),"utf-8")
        d[u"lat"]=unicode(str(lat),'utf-8')
        return d
    else:
        print url
        return None
'''
    key:关键词
    radius:半径
    lat:纬度
    lng:经度
'''
def getPOI(key,radius,lat,lng):
    ak = u'BjZFyCBFktfZmdj7SVP98fEFx78KzFn4'
    #ak=u'skS8wg9wP1VVFk2iuDuQATzoWKMb8FuY'
    #ak=u'AKsr88dgGDK8d74q7wTRbhiSb567HVmA'
    key = urllib2.quote(key)
    hd = HtmlDownloader.HtmlDownloader()
    ju =  JsonUtils.JsonUtils()
    url = 'http://api.map.baidu.com/place/v2/search?scope=2&query=%s&location=%s,%s&radius=%s&output=json&ak=%s&page_size=20' %(key,lat,lng,radius,ak)
    #print url
    res = hd.download(url)
    while(res is None):
        res = hd.download(url)
        print "retrying...",url
    res = unicode(res,'utf-8')
    data = ju.readStr(res)
    status = data[u'status']
    total = u'0'
    L =[]   
    #返回成功
    sss=u""
    index = 1
    if status==0:
        for poi in data[u'results']:
            name = poi[u'name']
            location = poi[u'location']
            address = poi[u'address']
            location = unicode(ju.writeJson2Str(location),'utf-8')
            sss = sss+unicode(str(index),'utf-8')+u":" + name+u"——"+address+u"——"+location
            index = index+1
        return data,sss
    else:
        return None
        
'''
    q:关键词
    radius:半径
'''
def getPOI2(q,region):
    q = q.encode('utf-8')
    region = region.encode('utf-8')
    L = []
    ak = u'BjZFyCBFktfZmdj7SVP98fEFx78KzFn4'
    #ak=u'skS8wg9wP1VVFk2iuDuQATzoWKMb8FuY'
    #ak=u'AKsr88dgGDK8d74q7wTRbhiSb567HVmA'
    q = urllib2.quote(q)
    region = urllib2.quote(region)
    #hd = HtmlDownloader.HtmlDownloader()
    #http://api.map.baidu.com/place/v2/search?query=购物中心&region=天津&city_limit=true&output=json&ak=BjZFyCBFktfZmdj7SVP98fEFx78KzFn4&page_num=0
    baseUrl = 'http://api.map.baidu.com/place/v2/search?query=%s&region=%s&city_limit=true&output=json&ak=%s&page_num=' %(q,region,ak)
    page = 0
    total= 1
    while page*10 < total:
        url = baseUrl+unicode(str(page),'utf-8')
        print url
        res = HtmlDownloader.download(url)
        while(res is None):
            res = HtmlDownloader.download(url)
            print "retrying...",url
        res = unicode(res,'utf-8')
        data = JsonUtils.readStr(res)
        status = data[u'status']
        message = data[u'message']
        if status==0 and message=='ok':
            #返回成功
            L.extend(data[u'results'])
            total = data[u'total']
            page = page + 1
        else:
            #失败
            print u"查询失败",message
            return L
    return L
if __name__=='__main__':
    q = u"商场"
    region = u'天津'
    #pos = getPos(addr,'天津')
    #print pos
    datas =  getPOI2(q,region)
    print len(datas)
    for data in datas:
        print data[u'name'],json.dumps(data[u'location']),data[u'address']