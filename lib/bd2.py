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

if __name__ == "__main__":
    cityID = 332
    wd = '商场'
    params=[[u"poiName",u'名称'],[u'poiAreaName',u"区"],[u'poiAddress',u'详细地址'],[u"poiJWD_X",u"经度"],[u"poiJWD_Y",u"纬度"]]
    #url = 'http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E5%95%86%E5%9C%BA&c=332&src=0&wd2=&sug=0&l=12&b=(13029204.58,4698610.67;13091156.58,4716402.67)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&tn=B_NORMAL_MAP&nn=0&u_loc=12478399,4472752&ie=utf-8&t=1499840034489'
    #url = 'http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=spot&from=webmap&c=332&wd=%E5%95%86%E5%9C%BA&wd2=&pn=0&nn=0&db=0&sug=0&addr=0&pl_data_type=shopping&pl_sub_type=%E5%95%86%E5%9C%BA&pl_price_section=0%2C%2B&pl_sort_type=&pl_sort_rule=0&pl_discount2_section=0%2C%2B&pl_groupon_section=0%2C%2B&pl_cater_book_pc_section=0%2C%2B&pl_hotel_book_pc_section=0%2C%2B&pl_ticket_book_flag_section=0%2C%2B&pl_movie_book_section=0%2C%2B&pl_business_type=shopping&pl_business_id=&da_src=pcmappg.poi.page&on_gel=1&src=7&gr=3&l=12&rn=50&tn=B_NORMAL_MAP&u_loc=12480272,4474029&ie=utf-8&b=(13021268.58,4703474.67;13083220.58,4721266.67)&t=1499844315282'
    #url = 'http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=con&from=webmap&c=332&wd=%E5%95%86%E5%9C%BA&wd2=&pn=5&nn=50&db=0&sug=0&addr=0&pl_data_type=shopping&pl_sub_type=%E5%95%86%E5%9C%BA&pl_price_section=0%2C%2B&pl_sort_type=&pl_sort_rule=0&pl_discount2_section=0%2C%2B&pl_groupon_section=0%2C%2B&pl_cater_book_pc_section=0%2C%2B&pl_hotel_book_pc_section=0%2C%2B&pl_ticket_book_flag_section=0%2C%2B&pl_movie_book_section=0%2C%2B&pl_business_type=shopping&pl_business_id=&da_src=pcmappg.poi.page&on_gel=1&src=7&gr=3&l=11&tn=B_NORMAL_MAP&u_loc=12480272,4474029&ie=utf-8&b=(12985364.58,4696370.67;13109268.58,4731954.67)&t=1499844727029'
    #baseUrl = 'http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=spot&from=webmap&c=332&wd=%E5%95%86%E5%9C%BA&wd2=&nn=0&db=0&sug=0&addr=0&pl_data_type=shopping&pl_sub_type=%E5%95%86%E5%9C%BA&pl_price_section=0%2C%2B&pl_sort_type=&pl_sort_rule=0&pl_discount2_section=0%2C%2B&pl_groupon_section=0%2C%2B&pl_cater_book_pc_section=0%2C%2B&pl_hotel_book_pc_section=0%2C%2B&pl_ticket_book_flag_section=0%2C%2B&pl_movie_book_section=0%2C%2B&pl_business_type=shopping&pl_business_id=&da_src=pcmappg.poi.page&on_gel=1&src=7&gr=3&l=9&rn=50&tn=B_NORMAL_MAP&u_loc=12480272,4474029&ie=utf-8&b=(12817812.58,4636594.67;13313428.58,4778930.67)&t=1499845484298&pn='
    #baseUrl = 'http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=con&from=webmap&c=%s&wd=%s&wd2=&nn=%s&db=0&sug=0&addr=0&da_src=pcmappg.poi.page&on_gel=1&src=7&gr=3&l=9&rn=%s&tn=B_NORMAL_MAP&ie=utf-8&t=1499845484298'
    uri = 'http://map.baidu.com/'
    pn = 19
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
            CsvUtils.writeList2File("F:\\ads.csv",L,params)    
        except:
            print "error",pn
        else:
            pass