# -*- coding: utf-8 -*-
import time,os
import random

def Cardthanbeast():
    print "卡比獸的招式："
    Trick=["破壞死光","地震","泰山壓頂"]
    for f in range(0,3):
        print Trick[f]
        time.sleep(1)
#

#for f in range(0,3):
    #Cardthanbeast() 

def Firechicks(s):
    print "火稚雞："
    time.sleep(1)
    print "使出："
    flame=["噴射火焰","啄攻擊","火花"]
    print flame[s]
#
#n=random.randint(0,2)

#Firechicks(n)   
#Firechicks(n)

#

def Charizard(s,name,status):
    print "噴火龍"
    time.sleep(1)
    print "對 %s 使出：" %(name)
    flame1=["噴射火焰","衝擊","火花"]
    print flame1[s]
    if status==0:
        print "失敗"
    else:
        print "成功"

#
#s is num
#name is str
#status is num


#n=random.randint(0,2)
#a=random.randint(0,4)

#s=n
#na="will"
#f=a
#Charizard(s,na,f)

#

def Frozenbirds (s,name,status,number):
    print "急凍鳥"
    time.sleep(1)
    print "對 %s 使出：" %(name)
    flame1=["急凍光線","暴風雪","高速移動"]
    print flame1[s]
    if status==0:
        print "失敗"
    else:
        print "成功"
    if status!=0:
        print number    
    
#


n=random.randint(0,2)
a=random.randint(0,4)
h=random.randint(34,1000)

s=n
na="皮卡丘"
f=a
num=h
Frozenbirds(s,na,f,num)





