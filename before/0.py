#!/usr/bin/python
# -*- coding: utf-8 -*-
import time,os
import paho.mqtt.client as mqtt
import datetime
from ITRI import JCSOUND

jcsound=JCSOUND()
now=datetime.datetime.now()
hours=now.strftime("%I")
for x in range(0,9):
	text = "現在時間是0%s點鐘" % x
	jcsound.run_sound(text)
	time.sleep(20)
for x in range(10,24):
	text = "現在時間是%s點鐘" % x
	jcsound.run_sound(text)
	time.sleep(20)

