# -*- coding:utf-8 -*-
import json
import os
import urllib2
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')

## http://api.map.baidu.com/place/v2/search?query=银行&bounds=39.615,116.404,39.975,116.414&page_size=20&page_num=0&output=json&ak=<KEY>
##  116.110,39.713   116.699,40.154

class BaiDuPOI(object):
    #par = BaiDuPOI(u'公交站',loc_to_use)
    def __init__(self,itemy,loc):
        self.itemy = itemy
        self.loc = loc
    #获得urls
    def urls(self):
        api_key = baidu_api
        urls = []
        for pages in range(0,20):
            url = 'http://api.map.baidu.com/place/v2/search?query=' + self.itemy + '&bounds=' + self.loc +'&page_size=20&page_num=' + str(pages) + '&output=json&ak=' + api_key
            urls.append(url)
        return urls

    def baidu_search(self):
        json_sel = []
        for url in self.urls():
            print url
            json_obj = urllib2.urlopen(url)
            data = json.load(json_obj)       
            for item in data['results']:
                jname = item["name"]
                jname = jname.replace(","," ")
                jlat = item["location"]["lat"]
                jlng = item["location"]["lng"]
                jaddress = item['address']
                jaddress = jaddress.replace(",","")
                js_sel = jname +',' + jaddress+','+str(jlat) + ',' + str(jlng)
                json_sel.append(js_sel)
        return json_sel

class LocaDiv(object):    
    #loc = LocaDiv('31.26,120.55,31.38,120.76',0.05)
    def __init__(self,loc_all,divd):
        self.loc_all = loc_all
        self.divd = divd
    #获得纬度的列表
    def lat_all(self):
        #31.26 纬度 西南角
        lat_sw = float(self.loc_all.split(',')[0])
        #31.38 纬度 东北角
        lat_ne = float(self.loc_all.split(',')[2])
        lat_list = [str(lat_ne)]
        while lat_ne-lat_sw >= 0:
            m = lat_ne - self.divd
            lat_ne = lat_ne - self.divd
            lat_list.append('%.2f' % m)
        return sorted(lat_list)
    #获得精度的列表
    def lng_all(self):
        lng_sw = float(self.loc_all.split(',')[1])
        lng_ne = float(self.loc_all.split(',')[3])
        lng_list = [str(lng_ne)]
        while lng_ne-lng_sw >= 0:
            m = lng_ne - self.divd
            lng_ne = lng_ne - self.divd
            lng_list.append('%.2f' % m)
        return sorted(lng_list)
    
    def ls_com(self):
        l1 = self.lat_all()
        l2 = self.lng_all()
        ab_list = []
        for i in range(0,len(l1)):
            a = str(l1[i])
            for i2 in range(0,len(l2)):
                b = str(l2[i2])
                ab = a+','+b
                ab_list.append(ab)
        return ab_list
    def ls_row(self):
        l1 = self.lat_all()
        l2 = self.lng_all()        
        ls_com_v = self.ls_com()
        ls = []
        for n in range(0,len(l1)-1):
            for i in range(len(l2)*n,len(l2)*(n+1)-1):
                a = ls_com_v[i]
                b = ls_com_v[i+len(l2)+1]
                ab = a+','+b
                ls.append(ab)
        return ls 
        
if __name__ == '__main__':  
    params = [[],[],[],[]]
    baidu_api = 'BjZFyCBFktfZmdj7SVP98fEFx78KzFn4' #这里填入你的百度API
    print u"开始爬数据，请稍等..."
    start_time = time.time()
    loc = LocaDiv('39.06,117.06,39.19,117.28',0.05)# 填入爬取区域坐标（这个坐标是苏州市城区区域坐标）、子区域长宽
    locs_to_use = loc.ls_row()
    for loc_to_use in locs_to_use:
        par = BaiDuPOI(u'商场',loc_to_use)                #请修改这里的类型参数
        a = par.baidu_search()
        doc = open(u'f:\\sofang\\POI\\商场.csv','a')                   #请修改这里的保存文件名，爬取完毕后请用记事本打开并保存下CSV文件，否则会乱码
        for ax in a:
            doc.write(ax)
            doc.write('\n')
        doc.close
    end_time = time.time()
    print u"数据爬取完毕，用时%.2f秒" % (end_time - start_time)