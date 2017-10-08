# -*- coding: utf-8 -*-
print "kiki"
x=range(0,5)
name=["jaccy","vicky","xuan","kiki","will"]

for number in x:
    print name[number]
    
for number in x:
    if name[number]=="kiki" or name[number]=="xuan":
        print "姊姊"


    if name[number]=="jaccy" or name[number]=="will":
        print "男生"
    else:
        print "女生"

    if name[number]=="jaccy" or name[number]=="vicky":
        print "大人" 
    

    if name[number]=="kiki" or name[number]=="xuan" or name[number]=="will":
        print "小孩"

