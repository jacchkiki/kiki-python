# -*- coding: utf-8 -*-
import time

class dog:
    name=""
    color=""
    s=0

    def dogname(self,sg):
        self.name="kiki"
        self.name=sg

    
    def dogcolor(self,sn):
        self.color="blue"
        self.color=sn
    def doggogo(self):
        self.s=self.s+1

    def dogbackback(self):
        self.s=self.s-1

    def doggogo2(self,fg):
        for gh in range(0,fg):
           self.doggogo()

    def dogbackback2(self,ut):
        for gh in range(0,ut):
           self.dogbackback()
     
    def wheredog(self):
        print self.s
        print self.name
        print self.color



la=dog()
la.dogname("will")
la.dogcolor("紅色")
la.doggogo2(2)
la.wheredog()

la.doggogo2(3)
la.wheredog()

la.doggogo2(5)
la.wheredog()

la.dogbackback()
la.wheredog()



