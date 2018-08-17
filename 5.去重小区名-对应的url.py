# coding=utf-8

import codecs
f = codecs.open(u"F:\\sofang2\\2.省_城市_对应URL.txt",'r','utf-8')
lines = f.readlines()
#对每一个city 每一个city整理一个文件
for line in lines[::]:
    line = line.strip('\r\n')
    shenName = line.split(u'^')[0]
    cityName = line.split(u'^')[2]
    cityUrl = line.split(u'^')[3]
    f1 = codecs.open(u'F:\\sofang2\\4.'+shenName+u"_"+cityName+u'-小区名-对应url-价格.txt','r','utf-8')
    f2 = codecs.open(u'F:\\sofang2\\5.'+shenName+u"_"+cityName+u'-小区名-对应url-价格.txt','w','utf-8')
    lineslines = f1.readlines()
    S = set({})
    #对每一个小区
    for lineline in lineslines:
        xqUrl = lineline.split(',')[5]
        if xqUrl in S:
            print shenName,cityName,u'重复'
            continue
        else:
            f2.write(lineline)
            S.add(xqUrl)