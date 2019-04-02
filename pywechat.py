#coding:utf-8
import itchat
import time
from spider import getMessage,getEnglish,getJoke
itchat.auto_login(enableCmdQR=2)
print 'login_success11111!!!!!!!!!'
users=itchat.search_friends(name=u'李全平')
print users
userName=users[0]['UserName']
def getgroup(g_name):
#    group=itchat.get_chatrooms(update=True)
#    for g in group:
#        if g['NickName']==g_name:
#            name=g['UserName']
#            return  name
#    return ''
    df=itchat.search_chatrooms(name=g_name)
    return df[0]['UserName']
group=getgroup("动次打次我们家")
print group
userName=group

def sendweather():

    res=getMessage()
    print res[0],res[1]
    mes=u"小宝贝，今天是%s\n今天的温度为%s度\n"%(res[1].strip(),res[0].strip())
    for i in res[2]:
        print i.text
        mes=mes+i.text.encode("utf-8")
    itchat.send(mes,userName)
    shijian=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    print shijian,userName
    print mes

def sendEnglish():
    content,note=getEnglish()
    itchat.send(content,userName)
    itchat.send(note,userName)

    shijian=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    print shijian,userName
    print note
    print content
def sendjoke():
    joke=getJoke().decode('unicode-escape')
    itchat.send(joke,userName)

    shijian=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    print shijian,userName
    print joke
sendweather()
time.sleep(10)
sendEnglish()
time.sleep(10)
n=30
while n>0:
    sendjoke()
    time.sleep(60*5)
    n-=1
