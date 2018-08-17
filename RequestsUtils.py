#coding:utf-8
import requests
import random
#此处修改头字段,自己用f12查看谷歌浏览器下自己的浏览器头信息，可以让根据目标站点而写的head会更好
headers = {
    'Host':"map.baidu.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
}
proxy1 = {"http": "1.171.57.170:3128"}
proxy2 = {"http": "148.251.133.62:3128"}

my_proxies = [proxy1,proxy2]

def getProxy():
    datas={
        'tid':'559464980977595',
        'num':1
    }
    proxyUrl='http://vtp.daxiangdaili.com/ip'
    res = requests.get(proxyUrl,params=datas)
    print res.url
    print res.status_code
    print res.text
    return res.text.split('\r\n')[0]
#发起请求,记得取消注释
def get_request(url,headers):
    #可设置代理
    i = random.randint(0,len(my_proxies)-1)
    proxies = my_proxies[i]
    res=requests.get(url,headers=headers,proxies=getProxy(), timeout=10)
    print res.url
    print res.status_code
    return html.text

if __name__ == '__main__':
    url = "http://www.baidu.com"
    get_request(url,headers)
