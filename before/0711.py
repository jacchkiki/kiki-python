# -*- coding: utf-8 -*-
import redis
s = redis.StrictRedis(host='192.168.1.113', port=6379, db=0)

x=range(0,3)
kiki=["剪刀","石頭","布"]

for d in x:
    d1=str(d)
    s.set('kiki'+d1, kiki[d])
    
    #print kiki[d]



for d in x:
    d2=str(d)
    will_play=s.get('will'+d2 )
    kiki_play=kiki[d]
    print will_play,kiki_play
    print "比賽結果"
    
    if will_play=="石頭" and kiki_play=="石頭":
        print "平手"
        
    if will_play=="石頭" and kiki_play=="布":
        print "kiki win"
        
    if will_play=="石頭" and kiki_play=="剪刀":
        print "will win"
    
    if will_play=="剪刀" and kiki_play=="剪刀":
        print "平手"
        
    if will_play=="剪刀" and kiki_play=="布":
        print "will win"
        
    if will_play=="剪刀" and kiki_play=="石頭":
        print "kiki win"
    
    if will_play=="布" and kiki_play=="布":
        print "平手"
    
    if will_play=="布" and kiki_play=="石頭":
        print "will win"
    
    if will_play=="布" and kiki_play=="剪刀":
        print "kiki win"
    
   
    
