# -*- coding: utf-8 -*-
import time,os
import random

def love():
    kiki=["剪刀","石頭","布"]
    n=random.randint(0,2)
    return kiki[n]


def jacch():
    kiki=["上","下","左","右"]
    n=random.randint(0,3)
    return kiki[n]

p1=love()
p2=love()
print "%s %s" % (p1,p2)

if p1!=p2:
    p1=jacch()
    p2=jacch()
    print "%s %s" % (p1,p2)


    
