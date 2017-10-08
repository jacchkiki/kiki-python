import time ,os
print "kiki"
y=10
print "kiki is %d years old."% y
name=["vicky","jacch","xuan","kiki","will"]
x=range(0,5)
for number in x:
    print name[number]

for number in x:
    if name[number]=="jacch":
        print "爸爸"
    time.sleep(60)
    
    if name[number]=="vicky":
        print "媽媽"
    time.sleep(60)
    
    if name[number]=="will":
        print "弟弟"
    time.sleep(60)
