# -*- coding: utf-8 -*-
import time

class monkey:
    name=""
    color=""
    s=0

    def monkeyname(self,sg):
        self.name="kiki"
        self.name=sg

    
    def monkeycolor(self,sn):
        self.color="blue"
        self.color=sn
    def monkeygogo(self):
        self.s=self.s+1
        time.sleep(0.1)


    def monkeybackback(self):
        self.s=self.s-1
        time.sleep(0.1)

    def monkeygogo2(self,fg):
        for gh in range(0,fg):
           self.monkeygogo()

    def monkeybackback2(self,ut):
        for gh in range(0,ut):
           self.monkeybackback()
     
    def wheremonkey(self):
        print self.s
        print self.name
        print self.color



la=monkey()
la.monkeyname("will")
la.monkeycolor("紅色")
la.monkeygogo2(100)
la.wheremonkey()
la.monkeybackback2(91)
la.wheremonkey()


