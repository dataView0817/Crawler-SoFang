# coding=utf-8
import urllib,urllib2,cookielib
import sys
def download(uri,parameter):
    parameter = urllib.urlencode(parameter)  
    print parameter
    ret = urllib.urlopen("%s?%s"%(uri, parameter))  
    code = ret.getcode()  
    if code ==200:
        ret_data = ret.read() 
        return  ret_data
    else:
        return None
if __name__=='__main__':
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

    uri = 'http://map.baidu.com/'  

    parameter = urllib2.urlencode(parameter)  
    print parameter
    ret = urllib.urlopen("%s?%s"%(uri, parameter))  
    code = ret.getcode()  
    ret_data = ret.read() 
    print ret_data