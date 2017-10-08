import time,os
print "kiki"
x=range(0,3)
fruit=["orange","apple","banana"]
will=["vicky","xuan","kiki"]
love=["dance","cook","write"]


for jacch in x:
    print will[jacch]
    
for jacch in x:
    print "%s %s" % (will[jacch],love[jacch])

for jacch in x:
    print "%s %s %s" % (will[jacch],love[jacch],fruit[jacch])

x=range(3)
fruit.append("peach")
love.append("read")
will.append("Andy")

for jacch in x:
    print "%s %s %s " % (will[jacch],love[jacch],fruit[jacch])

y=range(0,100)
for jacch in y:
    print y[jacch]
    

z=range(0,1000)
for jacch in z:
    print z[jacch]

p=range(0,10000)
for jacch in p:
    print p[jacch]



