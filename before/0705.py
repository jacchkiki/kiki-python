import time,os
from ITRI import JCSOUND
jcsound=JCSOUND()


x=range(0,3)
fruit=["peach","banana","apple"]
will=["kiki","xuan","vicky"]
love=["sing","run","dance"]

for jacch in x:
    print "%s like %s like %s" % (will[jacch],fruit[jacch],love[jacch])

fruit.append("orange")

print will[0]
print will[1]
print will[2]

print fruit[0]
print fruit[1]
print fruit[2]

print love[0]
print love[1]
print love[2]

for jacch in x:
    print will[jacch]

for jacch in x:
    print "%s %s" % (will[jacch],love[jacch])

for jacch in x:
    print "%s %s %s" % (will[jacch],love[jacch],fruit[jacch])
    happy="%s %s %s" % (will[jacch],love[jacch],fruit[jacch])
    jcsound.run_sound(happy)
    time.sleep(1)
