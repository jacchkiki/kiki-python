# -*- coding: utf-8 -*-
print "kiki"
x=range(0,3)
print x
fruit=["apple","orange","banana"]
for number in x:
    print fruit[number]

    if fruit[number]=="apple":
        print "red"

    if fruit[number]=="orange":
        print "orange"

    if fruit[number]=="banana":
        print "yellow"

fruit.append("peach")
x.append(3)
print x
for number in x:
    if fruit[number]=="peach":
        print "pink"
