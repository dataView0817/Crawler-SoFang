# encoding=utf-8
import xlwt
import codecs
import os
import os.path

f = codecs.open(u"F:\\sofang2\\2.省_城市_对应URL.txt",'r','utf-8')
lines = f.readlines()
#对每一个city
for line in lines[303:304:1]:
    line = line.strip('\r\n')
    shenName = line.split(u'^')[0]
    cityName = line.split(u'^')[2]
    if cityName==u"天津":
        continue
    cityUrl = line.split(u'^')[3]
    print shenName,cityName
    os.mkdir(u"F:\\sf_bd\\"+shenName+"_"+cityName) 
    path = u"F:\\sofang2\\6."+shenName+u"_"+cityName+u"-小区名-对应url-价格-经纬度-住户数.txt"
    path2 = u"F:\\sf_bd\\"+shenName+u"_"+cityName+u"\\"+shenName+u"_"+cityName+u"-小区名-对应url-价格-经纬度-住户数.xls"
    
    
    if os.path.exists(path2):#如果文件存在
        continue
        
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet')
    
    f1 = codecs.open(path,'r','utf-8')
    lineslines = f1.readlines()
    f1.close()
    S=set()
    for i in range(0,len(lineslines)):
        lineline = lineslines[i]
        if lineline.find('^')==-1:
            continue
        xqName = lineline.split("^")[0]
        areaName = lineline.split("^")[3]
        xqAddr = lineline.split("^")[4]
        jwd = lineline.split("^")[5]
        zhuHuShu = lineline.split("^")[6]
        xqPrice = lineline.split("^")[7]
        xqUrl = lineline.split("^")[8]
        areaUrl = lineline.split("^")[9]
        if xqUrl in S:
            continue
        S.add(xqUrl)
        ws.write(i, 0, xqName)
        ws.write(i, 1, shenName)
        ws.write(i, 2, cityName)
        ws.write(i, 3, areaName)
        ws.write(i, 4, xqAddr)
        ws.write(i, 5, jwd)
        ws.write(i, 6, zhuHuShu)
        ws.write(i, 7, xqPrice)
        ws.write(i, 8, xqUrl)
        ws.write(i, 9, areaUrl)
        
    wb.save(path2)
