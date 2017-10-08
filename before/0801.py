# -*- coding: utf-8 -*-
import time,os
import random

def hr():
    s=random.randint(0,2)
    will=["剪刀","石頭","布"]
    return will[s]

def ht():
    s=random.randint(0,3)
    will=["上","下","左","右"]
    return will[s]

def o(kiki_play,will_play):
    if will_play=="石頭" and kiki_play=="石頭":
        print "平手"
        
    if will_play=="石頭" and kiki_play=="布":
        print "kiki win"
        
    if will_play=="石頭" and kiki_play=="剪刀":
        print "will win"
    
    if will_play=="剪刀" and kiki_play=="剪刀":
        print "平手"
        
    if will_play=="剪刀" and kiki_play=="布":
        print "will win"
        
    if will_play=="剪刀" and kiki_play=="石頭":
        print "kiki win"
    
    if will_play=="布" and kiki_play=="布":
        print "平手"
    
    if will_play=="布" and kiki_play=="石頭":
        print "will win"
    
    if will_play=="布" and kiki_play=="剪刀":
        print "kiki win"


def v():
    one=hr()
    two=hr()
    if one!=two:
        three=ht()
        four=ht()
        if three==four:
            o(one,two)
            print "%s %s %s %s"% (one,two,three,four)

def q(c):
    l=c/2+1
    print l
    for h in range(0,l):
        v()

q(17)

dic={"Scissors":"剪刀","stone":"石頭","cloth":"布"}
print dic["Scissors"]
