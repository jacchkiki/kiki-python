# -*- coding: utf-8 -*-
import time
import random

def ah():
    a=random.randint(0,2)
    ta=["剪刀","石頭","布"]
    return ta[a]

g=ah
print g

class house:
    def dooropen(self):
        dooropen="打開門"
        return dooropen

    def doorclose(self):
        doorclose="關上門"
        return doorclose


fd=house()
sp=fd.dooropen()
ae=fd.doorclose()
print "%s %s" % (sp,ae)
