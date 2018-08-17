# coding=utf-8
import urllib2,cookielib
import sys

'''
    下载一个网页，返回该网页上的内容。如果抛出异常，则返回None
'''
def download(url):
    if url is None:
        return None
    try:
        response = urllib2.urlopen(url)
    except :
        info=sys.exc_info()
        print info[0],":",info[1]
        return None
    else:
        if response.getcode() != 200:
            return None
        return response.read()
    finally:
        pass

def download2(url):
    request = urllib2.Request(url)
    request.add_data('a','1')
    request.add_header('User-Agent','Mozilla/5.0')
    response = urllib2.urlopen(request)

def download3(url):
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)

    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    response = urllib2.urlopen("http://www.baidu.com")

def download4(url):
    if url is None:
        return None
    try:
        httpsHandler = urllib2.HTTPSHandler()
        opener = urllib2.build_opener(httpsHandler)
        urllib2.install_opener(opener)

        request = urllib2.Request(url)
        request.add_header('User-Agent','Mozilla/5.0')
        response = urllib2.urlopen(request)
    except :
        info=sys.exc_info()
        print info[0],":",info[1]
        return None
    else:
        if response.getcode() != 200:
            return None
        return response.read()
    finally:
        pass

import codecs
import json
if __name__ == "__main__":
    hd = HtmlDownloader()
    url = 'http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E5%95%86%E5%9C%BA&c=332&src=0&wd2=&sug=0&l=12&b=(13029204.58,4698610.67;13091156.58,4716402.67)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&tn=B_NORMAL_MAP&nn=0&u_loc=12478399,4472752&ie=utf-8&t=1499840034489'
    print hd.download4(url)