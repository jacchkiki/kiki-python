# -*- coding: utf-8 -*-
import time,os
import random

def ju():
    ax=["剪刀","石頭","布"]
    sr=random.randint(0,2)
    return ax[sr]

df=ju()
print df

class car:
    def up():
        up="上"
        return up

    def down():
        se="down"
        return se

    def left():
        da="left"
        return da
    
    def right():
        right="右"
        return right

    def frant():
        frant="前"
        return frant

    def freack():
        freack="後"
        return freack


aw=car()
print aw
