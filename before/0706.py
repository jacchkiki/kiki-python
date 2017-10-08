import time,os
x=range(0,3)
fruit=["orange","apple","banana"]
love=["vicky","kiki","xuan"]
will=["write","jump","run"]
print fruit[0]
print fruit[1]
print fruit[2]

print love[0]
print love[1]
print love[2]

print will[0]
print will[1]
print will[2]

for jacch in x:
    print "%s %s" % (will[jacch],love[jacch])

    
for jacch in x:
    print "%s %s %s" % (will[jacch],fruit[jacch],love[jacch])

for jacch in x:
    print fruit[jacch]

    
for jacch in x:
    print will[jacch]

for jacch in x:
    print love[jacch]

x.append(3)
fruit.append("peach")
love.append("read")
will.append("Andy")

for jacch in x:
    print "%s %s %s " % (will[jacch],love[jacch],fruit[jacch])
    time.sleep(1)
