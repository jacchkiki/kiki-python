import time,os
x=range(0,3)
fruit=["orange","apple","banana"]
will=["kiki","vicky","xuan"]
love=["run","cook","dance"]

for jacch in x:
    print will[jacch]

for jacch in x:
    print "%s %s" % (will[jacch],love[jacch])


for jacch in x:
    print "%s %s %s" % (will[jacch],love[jacch],fruit[jacch])

x=range(3)
fruit.append("pench")
will.append("dolls")
love.append("sing")

for jacch in x:
    print "%s %s %s" % (will[jacch],love[jacch],fruit[jacch])
    #time.sleep(1)
    
y=range(0,100)
for jacch in y:
    print y[jacch]
    time.sleep(1)

z=range(0,100)
for jacch in z:
    print z[jacch]
