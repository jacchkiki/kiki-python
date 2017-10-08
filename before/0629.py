# -*- coding: utf-8 -*-
print "kiki"
x=range(0,5)
name=["jacch","vicky","xuan","kiki","will"]

for number in x:
    print name[number]

    if name[number]=="vicky" or name[number]=="jacch":
        print "大人"

    else:
        print "小孩"

    if name[number]=="will" or name[number]=="jacch":
        print "笨蛋男生"
    else:
        print "女生"
