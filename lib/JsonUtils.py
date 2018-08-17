# coding=utf-8
import json
import codecs
import sys
import os
jianGe = u'间隔'
def readFile(filePath):
    try:
        fin = codecs.open(filePath,'r','utf-8')
        str = fin.read()
        L=[]
        for s in str.split(jianGe):
            d = json.loads(s)
            L.append(d)
    except:
        info=sys.exc_info()  
        print info[0],":",info[1]
        return None 
    else:
        fin.close()
        return L
    finally:
        pass

def readFile2(filePath):
    res = []
    S=set([])
    datass = readFile(filePath)
    for datas in datass:
        for data in datas:
            if not data[u'网址'] in S:
                res.append(data)
            else:
                print data[u'网址'],"repeated..."
            S.add(data[u'网址'])
    return res
    
def readStr(str):
    try:
        res = json.loads(str)
    except:
        info=sys.exc_info()  
        print info[0],":",info[1]
        return None
    else:
        return res
        
def readStr2(str):
    try:
        str = formatJson(str)
        res = json.loads(str)
    except:
        info=sys.exc_info()  
        print info[0],":",info[1]
        return None
    else:
        return res

def writeJson2Str(j):
    return json.dumps(j)
    
def writeJson2File(filePath,datas):
    old_datas = readFile(filePath)
    if old_datas is not None:
        fin = codecs.open(filePath,'a','utf-8')
        str = jianGe + writeJson2Str(datas)
        fin.write(str)
        fin.close()
    else:
        fin = codecs.open(filePath,'w','utf-8')
        str = writeJson2Str(datas)
        fin.write(str)
        fin.close()

def formatJson(str):
    sss =  str.split(r';ZWD_CFG.SKUS=')[1]
    start= sss.find("{")
    end= sss.rfind("}")
    return sss[start:end+1:1]


html_cont='''
ZWD_CFG.SKUSINFO={"total":25000,"sku":[{"price":71.00,"price2":21.0,"properties":"1627207:28320;20509:28314","properties_name":"1627207:28320:白色;20509:28314:S","num":1000,"sku_id":3483818107687},{"price":71.00,"price2":21.0,"properties":"1627207:28320;20509:28315","properties_name":"1627207:28320:白色;20509:28315:M","num":1000,"sku_id":3483818107688},{"price":71.00,"price2":21.0,"properties":"1627207:28320;20509:28316","properties_name":"1627207:28320:白色;20509:28316:L","num":1000,"sku_id":3483818107689},{"price":71.00,"price2":21.0,"properties":"1627207:28320;20509:28317","properties_name":"1627207:28320:白色;20509:28317:XL","num":1000,"sku_id":3483818107690},{"price":71.00,"price2":21.0,"properties":"1627207:28320;20509:6145171","properties_name":"1627207:28320:白色;20509:6145171:2XL","num":1000,"sku_id":3483818107691},{"price":71.00,"price2":21.0,"properties":"1627207:28341;20509:28314","properties_name":"1627207:28341:黑色;20509:28314:S","num":1000,"sku_id":3483818107692},{"price":71.00,"price2":21.0,"properties":"1627207:28341;20509:28315","properties_name":"1627207:28341:黑色;20509:28315:M","num":1000,"sku_id":3483818107693},{"price":71.00,"price2":21.0,"properties":"1627207:28341;20509:28316","properties_name":"1627207:28341:黑色;20509:28316:L","num":1000,"sku_id":3483818107694},{"price":71.00,"price2":21.0,"properties":"1627207:28341;20509:28317","properties_name":"1627207:28341:黑色;20509:28317:XL","num":1000,"sku_id":3483818107695},{"price":71.00,"price2":21.0,"properties":"1627207:28341;20509:6145171","properties_name":"1627207:28341:黑色;20509:6145171:2XL","num":1000,"sku_id":3483818107696},{"price":71.00,"price2":21.0,"properties":"1627207:3232484;20509:28314","properties_name":"1627207:3232484:天蓝色;20509:28314:S","num":1000,"sku_id":3483818107697},{"price":71.00,"price2":21.0,"properties":"1627207:3232484;20509:28315","properties_name":"1627207:3232484:天蓝色;20509:28315:M","num":1000,"sku_id":3483818107698},{"price":71.00,"price2":21.0,"properties":"1627207:3232484;20509:28316","properties_name":"1627207:3232484:天蓝色;20509:28316:L","num":1000,"sku_id":3483818107699},{"price":71.00,"price2":21.0,"properties":"1627207:3232484;20509:28317","properties_name":"1627207:3232484:天蓝色;20509:28317:XL","num":1000,"sku_id":3483818107700},{"price":71.00,"price2":21.0,"properties":"1627207:3232484;20509:6145171","properties_name":"1627207:3232484: 天蓝色;20509:6145171:2XL","num":1000,"sku_id":3483818107701},{"price":71.00,"price2":21.0,"properties":"1627207:28323;20509:28314","properties_name":"1627207:28323:粉色;20509:28314:S","num":1000,"sku_id":3483818107702},{"price":71.00,"price2":21.0,"properties":"1627207:28323;20509:28315","properties_name":"1627207:28323:粉色;20509:28315:M","num":1000,"sku_id":3483818107703},{"price":71.00,"price2":21.0,"properties":"1627207:28323;20509:28316","properties_name":"1627207:28323:粉色;20509:28316:L","num":1000,"sku_id":3483818107704},{"price":71.00,"price2":21.0,"properties":"1627207:28323;20509:28317","properties_name":"1627207:28323:粉色;20509:28317:XL","num":1000,"sku_id":3483818107705},{"price":71.00,"price2":21.0,"properties":"1627207:28323;20509:6145171","properties_name":"1627207:28323:粉色;20509:6145171:2XL","num":1000,"sku_id":3483818107706},{"price":71.00,"price2":21.0,"properties":"1627207:6872191;20509:28314","properties_name":"1627207:6872191:豆绿色;20509:28314:S","num":1000,"sku_id":3483818107707},{"price":71.00,"price2":21.0,"properties":"1627207:6872191;20509:28315","properties_name":"1627207:6872191:豆绿色;20509:28315:M","num":1000,"sku_id":3483818107708},{"price":71.00,"price2":21.0,"properties":"1627207:6872191;20509:28316","properties_name":"1627207:6872191:豆绿色;20509:28316:L","num":1000,"sku_id":3483818107709},{"price":71.00,"price2":21.0,"properties":"1627207:6872191;20509:28317","properties_name":"1627207:6872191:豆绿色;20509:28317:XL","num":1000,"sku_id":3483818107710},{"price":71.00,"price2":21.0,"properties":"1627207:6872191;20509:6145171","properties_name":"1627207:6872191:豆绿色;20509:6145171:2XL","num":1000,"sku_id":3483818107711}]};ZWD_CFG.SKUS={"total":25000,"sku":[{"price":71.00,"price2":21.0,"properties":"1627207:28320;20509:28314","properties_name":"1627207:28320:白色;20509:28314:S","num":1000,"sku_id":3483818107687},{"price":71.00,"price2":21.0,"properties":"1627207:28320;20509:28315","properties_name":"1627207:28320:白色;20509:28315:M","num":1000,"sku_id":3483818107688},{"price":71.00,"price2":21.0,"properties":"1627207:28320;20509:28316","properties_name":"1627207:28320:白色;20509:28316:L","num":1000,"sku_id":3483818107689},{"price":71.00,"price2":21.0,"properties":"1627207:28320;20509:28317","properties_name":"1627207:28320:白色;20509:28317:XL","num":1000,"sku_id":3483818107690},{"price":71.00,"price2":21.0,"properties":"1627207:28320;20509:6145171","properties_name":"1627207:28320:白色;20509:6145171:2XL","num":1000,"sku_id":3483818107691},{"price":71.00,"price2":21.0,"properties":"1627207:28341;20509:28314","properties_name":"1627207:28341:黑色;20509:28314:S","num":1000,"sku_id":3483818107692},{"price":71.00,"price2":21.0,"properties":"1627207:28341;20509:28315","properties_name":"1627207:28341:黑色;20509:28315:M","num":1000,"sku_id":3483818107693},{"price":71.00,"price2":21.0,"properties":"1627207:28341;20509:28316","properties_name":"1627207:28341:黑色;20509:28316:L","num":1000,"sku_id":3483818107694},{"price":71.00,"price2":21.0,"properties":"1627207:28341;20509:28317","properties_name":"1627207:28341:黑色;20509:28317:XL","num":1000,"sku_id":3483818107695},{"price":71.00,"price2":21.0,"properties":"1627207:28341;20509:6145171","properties_name":"1627207:28341:黑色;20509:6145171:2XL","num":1000,"sku_id":3483818107696},{"price":71.00,"price2":21.0,"properties":"1627207:3232484;20509:28314","properties_name":"1627207:3232484:天蓝色;20509:28314:S","num":1000,"sku_id":3483818107697},{"price":71.00,"price2":21.0,"properties":"1627207:3232484;20509:28315","properties_name":"1627207:3232484:天蓝色;20509:28315:M","num":1000,"sku_id":3483818107698},{"price":71.00,"price2":21.0,"properties":"1627207:3232484;20509:28316","properties_name":"1627207:3232484:天蓝色;20509:28316:L","num":1000,"sku_id":3483818107699},{"price":71.00,"price2":21.0,"properties":"1627207:3232484;20509:28317","properties_name":"1627207:3232484:天蓝色;20509:28317:XL","num":1000,"sku_id":3483818107700},{"price":71.00,"price2":21.0,"properties":"1627207:3232484;20509:6145171","properties_name":"1627207:3232484:天蓝色;20509:6145171:2XL","num":1000,"sku_id":3483818107701},{"price":71.00,"price2":21.0,"properties":"1627207:28323;20509:28314","properties_name":"1627207:28323:粉色;20509:28314:S","num":1000,"sku_id":3483818107702},{"price":71.00,"price2":21.0,"properties":"1627207:28323;20509:28315","properties_name":"1627207:28323:粉色;20509:28315:M","num":1000,"sku_id":3483818107703},{"price":71.00,"price2":21.0,"properties":"1627207:28323;20509:28316","properties_name":"1627207:28323:粉色;20509:28316:L","num":1000,"sku_id":3483818107704},{"price":71.00,"price2":21.0,"properties":"1627207:28323;20509:28317","properties_name":"1627207:28323:粉色;20509:28317:XL","num":1000,"sku_id":3483818107705},{"price":71.00,"price2":21.0,"properties":"1627207:28323;20509:6145171","properties_name":"1627207:28323:粉色;20509:6145171:2XL","num":1000,"sku_id":3483818107706},{"price":71.00,"price2":21.0,"properties":"1627207:6872191;20509:28314","properties_name":"1627207:6872191:豆绿色;20509:28314:S","num":1000,"sku_id":3483818107707},{"price":71.00,"price2":21.0,"properties":"1627207:6872191;20509:28315","properties_name":"1627207:6872191:豆绿色;20509:28315:M","num":1000,"sku_id":3483818107708},{"price":71.00,"price2":21.0,"properties":"1627207:6872191;20509:28316","properties_name":"1627207:6872191:豆绿色;20509:28316:L","num":1000,"sku_id":3483818107709},{"price":71.00,"price2":21.0,"properties":"1627207:6872191;20509:28317","properties_name":"1627207:6872191:豆绿色;20509:28317:XL","num":1000,"sku_id":3483818107710},{"price":71.00,"price2":21.0,"properties":"1627207:6872191;20509:6145171","properties_name":"1627207:6872191:豆绿色;20509:6145171:2XL","num":1000,"sku_id":3483818107711}]};ZWD_CFG.ColorCids='1627207';ZWD_CFG.SizeCids='20509,20518,20549,122508275,122216343';
'''
import JsonUtils
if __name__ == "__main__":
    #str="<!--KG_TAG_RES_START-->{dat{<>{}{}}{}a}<!--KG_TAG_RES_END-->"
    #print JsonUtils.formatJson(str)
    #html_cont = JsonUtils.formatJson(html_cont)
    #print html_cont
    #datas = [{u"姓名":u"张三",u"age":12},{u"姓名":u"张三",u"age":12},{u"姓名":u"张三",u"age":12}]
    #JsonUtils.writeJson2File("F:\\ddd.json",datas)
    datass = JsonUtils.readFile("F:\\ddd.json")
    print type(datass),len(datass)
    print type(datass[0]),len(datass[0])
    for data in datass[0]:
        print data
    #JsonUtils.writeJson2File("F:\\dda.json",datas)
    #JsonUtilswriteJson2File("F:\\dda.json",{u"姓名":u"张三",u"age":12})
    #datas  = JsonUtils.readFile("F:\\dda.json")
    #for data in datas:
    #    print type(data),data
    #datas = JsonUtils.readStr(html_cont)
    #print datas[u'total']
    #for sku in datas[u'sku']:
    #    print sku[u'price'],sku[u'price2'],sku[u'num'],sku[u'properties_name'].split(';')[0].split(':')[2],sku[u'properties_name'].split(';')[1].split(':')[2]
