# -*- coding: utf-8 -*-
print "kiki"
x=range(0,3)
name=["kiki","vicky","will"]
for number in x:
    print name[number]

for number in x:
    if name[number]=="kiki":
        print "妹妹"


    if name[number]=="vicky":
        print "媽媽"


    if name[number]=="will":
        print "弟弟"
n=0
a=0
while n<24:
    print "現在%d點鐘"% n
    n=n+1
    a=a+n

print a
