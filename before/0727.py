# -*- coding: utf-8 -*-
import time,os
import random

def bag():
    n=random.randint(0,2)
    kiki=["剪刀","石頭","布"]
    return kiki[n]


def bag1():
    n=random.randint(0,3)
    kiki=["上","下","左","右"]
    return kiki[n]

def s(kiki_play,will_play):
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
    

def f():
    p1=bag()
    p2=bag()
    if p1!=p2:
        p3=bag1()
        p4=bag1()
        if p3==p4:
            s(p1,p2)
            print "%s %s %s %s" % (p1,p2,p3,p4)



for d in range(0,10):
    f()
