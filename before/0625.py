# -*- coding: utf-8 -*-
import time,os
print "kiki"
x=range(0,3)
name=["kiki","vicky","will"]


for number in x:
    print name[number]

for number in x:
    if name[number]=="kiki":
        print "姊姊"

n=0
while n<24:
    text = "現在時間是%d點" % n
    print text
    n=n+1
    time.sleep(1)
