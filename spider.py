#coding:utf-8
import sys
import bs4
reload(sys)
sys.setdefaultencoding( 'utf-8' )
import random,re
import urllib3
import sys
import requests
from bs4 import BeautifulSoup


def getMessage():
    http=urllib3.PoolManager()
    url='http://tianqi.sogou.com/beijing'

    resp=http.request('get',url)

    html=resp.data
    #html=requests.get("http://tianqi.sogou.com/beijing/")
    res = BeautifulSoup(html,"html.parser")
    wendu = res.findAll("span",{"class":"num"})
    #print wendu[0].text
    date =  res.findAll("a",{"class":"date"})
    #print date[0].text
    tips=res.findAll("span",{"class":"info"})
    #for i in tips:
    #    print i.text
    weather=[wendu[0].text,date[0].text,tips]
    return weather
def getEnglish():
    url='http://open.iciba.com/dsapi/'
    resp=requests.get(url)

    content=resp.json()['content']
    note=resp.json()['note']
    return content,note
def fill2(ulist,html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find_all('div','article block untagged mb15 typs_hot'):
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find('div','content')
            tdss=tds('span')
            reg = re.compile('<[^>]*>')
            text=reg.sub('',str(tdss))
            regg = re.compile('\\[|\\]|\\n')
            text=regg.sub('',text)
            ulist.append(text)
def getHTMLText(url):
    try:
        headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        r = requests.get(url,headers=headers)
        r.raise_for_status()
        #r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print e
        print("faile")
        return ""
def getJoke():
    ulist=[]
    u='https://www.qiushibaike.com/text/page/'
    i=random.randint(1,13)
    url=u+str(i)+'/'
    print url
    html=getHTMLText(url)
   # print 'html:',html
    fill2(ulist,html)
    #print ulist
    k=random.randint(0,16)
    #print(str(ulist[k]))
    return str(ulist[k])
if __name__ == "__main__":
    #weather = getMessage()
    #content,note=getEnglish()
    #print content,note
    #print weather
    joke=getJoke()
    print joke.decode('unicode-escape')
