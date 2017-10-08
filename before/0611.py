# -*- coding: utf-8 -*-
import time,os
print "kiki"
y=10
print "kiki is %d years old."% y
x=range(0,3)
print x
name=["xuan","kiki","will"]

for number in x:
    print name[number]

for number in x:
    if name[number]=="kiki":
        print "姊姊"
        
for number in x:
    if name[number]=="will":
        print "弟弟"

        
for number in x:
    if name[number]=="xuan":
        print "神豬"
n=0
while True:
    print "現在%d點鐘"% n
    time.sleep(1)
    n=n+1

    if n==24:
        break

        
