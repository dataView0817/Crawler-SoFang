# coding=utf-8
import HtmlDownloader
import HtmlDownloader2
import urllib2
import JsonUtils
import json
import CsvUtils

parameter = {  
        "newmap": "1",  
        "reqflag": "pcmap",  
        "biz": "1",  
        "from": "webmap",  
        "da_par": "direct",  
        "pcevaname": "pc4.1",  
        "qt": "con",  
        "c": 332,            # 城市代码  
        "wd": '商场',       # 搜索关键词  
        "wd2": "",  
        "pn": 0,           # 页数  
        "nn": 0,  
        "db": "0",  
        "sug": "0",  
        "addr": "0",  
        "da_src": "pcmappg.poi.page",  
        "on_gel": "1",  
        "src": "7",  
        "gr": "3",  
        "l": "12",  
        "tn": "B_NORMAL_MAP",  
        # "u_loc": "12621219.536556,2630747.285024",  
        "ie": "utf-8",  
        # "b": "(11845157.18,3047692.2;11922085.18,3073932.2)",  #这个应该是地理位置坐标，可以忽略  
        "t": "1468896652886"  
} 

def getDatas(cityID,wd,path):
    params=[[u"poiName",u'名称'],[u'poiAreaName',u"区"],[u'poiAddress',u'详细地址'],[u"poiJWD_X",u"经度"],[u"poiJWD_Y",u"纬度"]]
    uri = 'http://map.baidu.com/'
    pn = 0
    while pn<600:
        try:
            L=[]
            para = parameter
            para['c'] = cityID
            para['wd'] = wd
            para['pn'] = pn
            para['nn'] = pn*10
            pn = pn+1
            content = HtmlDownloader2.download(uri,para)
            datas = JsonUtils.readStr(content)
            datas = datas[u'content']
            for data in datas:
                #区
                poiAreaName = data[u'area_name']
                #名称
                poiName = data[u'name']
                #poiAlias = data[u'alias']
                #地址
                poiAddress = data[u'addr']
                #详细地址
                #poiNormAddress = data[u'address_norm']
                #经纬度
                poiJWD_X = unicode(str(data[u'x']),'utf-8')
                poiJWD_Y = unicode(str(data[u'y']),'utf-8')
                poiJWD_X = poiJWD_X[:len(poiJWD_X)-2:1]+u"."+poiJWD_X[len(poiJWD_X)-2::1]
                poiJWD_Y = poiJWD_Y[:len(poiJWD_Y)-2:1]+u"."+poiJWD_Y[len(poiJWD_Y)-2::1]
                L.append({u"poiName":poiName,u"poiAreaName":poiAreaName,u"poiAddress":poiAddress,u"poiJWD_X":poiJWD_X,u"poiJWD_Y":poiJWD_Y})
            CsvUtils.writeList2File(path,L,params)    
        except:
            print "error",pn
            return 
        else:
            pass