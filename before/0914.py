# -*- coding: utf-8 -*-
import time

class tiger:
    name=""
    color=""
    s=0

    def tigername(self,sg):
        self.name="kiki"
        self.name=sg

    
    def tigercolor(self,sn):
        self.color="blue"
        self.color=sn
    def tigergogo(self):
        self.s=self.s+1
        time.sleep(1)


    def tigerbackback(self):
        self.s=self.s-1
        time.sleep(1)

    def tigergogo2(self,fg):
        for gh in range(0,fg):
           self.tigergogo()

    def tigerbackback2(self,ut):
        for gh in range(0,ut):
           self.tigerbackback()
     
    def wheretiger(self):
        print self.s
        print self.name
        print self.color



la=tiger()
la.tigername("will")
la.tigercolor("紅色")
la.tigergogo2(100)
la.wheretiger()
la.tigerbackback2(91)
la.wheretiger()


