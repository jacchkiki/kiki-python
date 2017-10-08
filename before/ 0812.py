# -*- coding: utf-8 -*-
import time
class duck:
    name=""
    color=""
    f=0

    def duckname(self,sg):
        self.name="kiki"
        self.name=sg

    
    def duckcolor(self,sn):
        self.color="blue"
        self.color=sn
    def duckgogo(self):
        self.f=self.f+1
        time.sleep(1)

    def duckbackback(self):
        self.f=self.f-1
        time.sleep(1)

    def duckgogo2(self,fg):
        for gh in range(0,fg):
           self.duckgogo()

    def duckbackback2(self,ut):
        for gh in range(0,ut):
           self.duckbackback()
     
    def whereduck(self):
        print self.f
        print self.name
        print self.color


la=duck()
la.duckname("will")
la.duckcolor("紅色")
la.duckgogo2(5)
la.whereduck()

la.duckgogo2(10)
la.whereduck()

la.duckbackback2(5)
la.whereduck()


  
