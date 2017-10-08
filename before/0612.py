#!/usr/bin/python
# -*- coding: utf-8 -*-
import time,os
import paho.mqtt.client as mqtt
import datetime
from ITRI import JCSOUND

jcsound=JCSOUND()
now=datetime.datetime.now()
hours=now.strftime("%I")

#text = "現在時間是%s點鐘" % hours
#jcsound.run_sound(aaa)

n=0

#while n<24:
#   text = "現在時間是%d點鐘" % n
#   jcsound.run_sound(text)

#   n=n+1
#   time.sleep(3)

#print "END"


m=1

while m<60:
    text = "現在時間是%d點%d分" % (n,m)
    jcsound.run_sound(text)

    m=m+1
    time.sleep(3)

print "END"
   
