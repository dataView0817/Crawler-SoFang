# coding=utf-8
import codecs
import sys

def writeList2File(filePath,datas,params):
    str_data=u""
    for param in params:
        str_data = str_data+param[1]+","
    str_data = str_data+"\r\n"
    for data in datas:
        for param in params:
            str_data = str_data + data[param[0]]+","
        str_data=str_data+"\r\n"

    old_data = readStrFromFile(filePath)
    if old_data is not None and old_data.strip()!="":
        str_data = old_data+u"\r\n"+str_data
    f = codecs.open(filePath,'w','utf-8')
    f.write(str_data)
    f.close()

def writeList2FileForBD(filePath,datas,shenCityArea):
    str_data=u""
    posInfo = shenCityArea[u'shenName']+u","+ shenCityArea[u'cityName']+u','+shenCityArea[u'areaName'] +u","
    str_data =u"省,市,区,名称,详细地址,经纬度" +"\r\n"
    for data in datas:
        str_data = str_data+posInfo
        str_data = str_data+data[u'name']+","+data[u'address'].replace(u",",u" ")+","+json.dumps(data[u'location']).replace(u",",u"")
        str_data = str_data+"\r\n"

    old_data = readStrFromFile(filePath)
    if old_data is not None and old_data.strip()!="":
        str_data = old_data+u"\r\n"+str_data
    f = codecs.open(filePath,'w','utf-8')
    f.write(str_data)
    f.close()
    
'''
    filePath:
    params:[["name","姓名"],[],[]]
'''
def readStrFromFile(filePath):
    try:
        fin = codecs.open(filePath,'r','utf-8')
        str = fin.read()
    except:
        info=sys.exc_info()  
        print info[0],":",info[1]
        return None 
    else:
        fin.close()
        return str
    finally:
        pass
import CsvUtils
import json
if __name__ == "__main__":
    #params=[[u"姓名",u"name"],[u"age",u"年龄"]]
    datas = [{u"name":u"张三",u"address":u'12',u'location':u'123'},{u"姓名":u"张三",u"age":'12'},{u"姓名":u"张三",u"age":'12'}]
    datas = [{u"name":u"张三",u"address":u'12',u'location':u'123'},{u"name":u"张三",u"address":u'12',u'location':u'123'},{u"name":u"张三",u"address":u'12',u'location':u'123'}]
    #CsvUtils.writeList2File("F:\\dda.csv",datas,params)
    #ju.writeJson2File("F:\\dda.json",{u"姓名":u"张三",u"age":12})
    #datas  = CsvUtils.readStrFromFile("F:\\dda.csv")
    #print datas
    shenCityArea={u"shenName":u"直辖市",u"cityName":u"天津",u"areaName":u""}
    CsvUtils.writeList2FileForBD(u"F:\\"+u'天津'+u"_"+u'商城'+".csv",datas,shenCityArea)