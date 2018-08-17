# coding=utf-8
import codecs
import json
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    
    '''
        将List输出到html文件中
            item是dict   表头是dict的key，每一行是一个item
            item不是dict 表头是项目
    '''
    def outputList2html(self,path,datas):
        if datas is None or len(datas)==0 or not isinstance(datas,list):
            return
        fout = codecs.open(path,'w','utf-8')
        fout.write(u"<html>")
        fout.write(u"<body>")
        fout.write(u'<table border="1" bordercolor="red">')
        
        fout.write(u"<tr>")
        fout.write(u"<td>"+u"记录数"+u"</td>")
        if isinstance(datas[0],dict):
            for key in datas[0]:
                fout.write(u"<td>"+key+u"</td>")
        else:
            fout.write(u"<td>"+u"项目"+u"</td>")
        fout.write(u"</tr>")
        
        i = 1
        for d in datas:
            fout.write(u"<tr>")
            fout.write(u"<td>"+str(i)+u"</td>")
            i = i+1
            if isinstance(d,dict):
                for key in d:
                    value = d[key]
                    if isinstance(value,unicode):
                        fout.write(u"<td>"+value+u"</td>")
                    else:
                        fout.write(u"<td>"+unicode(str(value),'utf-8')+u"</td>")
            elif isinstance(d,unicode):
                fout.write(u"<td>"+d+u"</td>")
            else :
                fout.write(u"<td>"+unicode(str(d),'utf-8')+u"</td>")
            fout.write(u"</tr>")
        
        fout.write(u'</table>')
        fout.write(u"</body>")
        fout.write(u"</html>")
        
        fout.close()

        
    '''
        将List输出到html文件中
            item是dict   表头是dict的key，每一行是一个item
            item不是dict 表头是项目
    '''
    def outputList2html2(self,path,datas,params):
        if datas is None or len(datas)==0 or not isinstance(datas,list):
            return
        fout = codecs.open(path,'w','utf-8')
        fout.write(u"<html>")
        fout.write(u"<body>")
        fout.write(u'<table border="1" bordercolor="red">')
        
        fout.write(u"<tr>")
        fout.write(u"<td>"+u"记录数"+u"</td>")
        if isinstance(datas[0],dict):
            for key in params:
                fout.write(u"<td>"+key+u"</td>")
        else:
            fout.write(u"<td>"+u"项目"+u"</td>")
        fout.write(u"</tr>")
        
        i = 1
        for d in datas:
            fout.write(u"<tr>")
            fout.write(u"<td>"+str(i)+u"</td>")
            i = i+1
            if isinstance(d,dict):
                for key in params:
                    value = d[key]
                    if isinstance(value,unicode):
                        fout.write(u"<td>"+value+u"</td>")
                    else:
                        fout.write(u"<td>"+unicode(str(value),'utf-8')+u"</td>")
            elif isinstance(d,unicode):
                fout.write(u"<td>"+d+u"</td>")
            else :
                fout.write(u"<td>"+unicode(str(d),'utf-8')+u"</td>")
            fout.write(u"</tr>")
        
        fout.write(u'</table>')
        fout.write(u"</body>")
        fout.write(u"</html>")
        
        fout.close()
        
        
        
    '''
        将List输出到html文件中
            item是dict   表头是dict的key，每一行是一个item
            item不是dict 表头是项目
        params是一个List，每个item是list [原来的属性名,要修改成的属性名]
    '''
    def outputList2html3(self,path,datas,params):
        if datas is None or len(datas)==0 or not isinstance(datas,list):
            return
        fout = codecs.open(path,'w','utf-8')
        fout.write(u"<html>")
        fout.write(u"<body>")
        fout.write(u'<table border="1" bordercolor="red">')
        
        fout.write(u"<tr>")
        fout.write(u"<td>"+u"记录数"+u"</td>")
        if isinstance(datas[0],dict):
            for param in params:
                fout.write(u"<td>"+param[1]+u"</td>")
        else:
            fout.write(u"<td>"+u"项目"+u"</td>")
        fout.write(u"</tr>")
        
        i = 1
        for d in datas:
            fout.write(u"<tr>")
            fout.write(u"<td>"+str(i)+u"</td>")
            i = i+1
            if isinstance(d,dict):
                for param in params:
                    value = d[param[0]]
                    if isinstance(value,unicode):
                        fout.write(u"<td>"+value+u"</td>")
                    else:
                        fout.write(u"<td>"+unicode(str(value),'utf-8')+u"</td>")
            elif isinstance(d,unicode):
                fout.write(u"<td>"+d+u"</td>")
            else :
                fout.write(u"<td>"+unicode(str(d),'utf-8')+u"</td>")
            fout.write(u"</tr>")
        
        fout.write(u'</table>')
        fout.write(u"</body>")
        fout.write(u"</html>")
        
        fout.close()
        
if __name__ == "__main__":
    datas=[{u"name":u"张中俊",u"age":u"12"},{u"name":u"张霉霉",u"age":u"123"}]
    params=[[u"age",u"姓名"],[u"name",u"年龄"]]
    print params[0][0]
    ho = HtmlOutputer()
    ho.outputList2html3("F:\\daass.html",datas,params)