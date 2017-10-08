import time,os
print "kiki"
x=range(0,3)
flavor=["apple","banana","peach"]
will=["kiki","xuan","vicky"]
print will[0]
print will[1]
print will[2]
for jacch in x:
    print "%s like %s" % (will[jacch],flavor[jacch])

y=range(0,4)
name=["a","b","c","d"]
name2=["w","x","y","z"]
for Happy in y:
    print "%s like %s" % (name2[Happy],name[Happy])
    time.sleep(1)
z=range(0,5)
yes=["e","f","g","h","i"]
no=["j","k","l","n","m"]
for Scott in z:
    print "%s like %s" % (no[Scott],yes[Scott])
    os.system("aplay jacch/sound/ff0831ec237c5d8a7fbe0f75a4c66281.wav")    
