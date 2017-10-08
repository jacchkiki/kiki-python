# -*- coding: utf-8 -*-
import time,os
print "kiki"
y=10
print "kiki is %d years old."% y
x=range(0,5)
name=["jacch","vicky","xuan","kiki","will"]

for number in x:
    print name[number]
    
if name[number]=="will":
    print "弟弟"
    time.sleep(1)

for number in x:
    if name[number]=="xuan":
        print "大姊"
    time.sleep(1)
    
for number in x:
    if name[number]=="kiki":
        print "姊姊"
    time.sleep(1)

n=0
while True:
    print "現在 %d 點鐘"% n
    time.sleep(1)
    n=n+1

    if n==10:
        break

a=True
print "a是真的"

b=false
print "b是假的"
