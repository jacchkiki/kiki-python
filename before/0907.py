# -*- coding: utf-8 -*-
import time

class car:
    g=0
    name=""
    color=""

    def carname(self,sk):
        self.name="kiki"
        self.name=sk

    def carcolor(self,al):
        self.color="blue"
        self.color=al

    def gogo(self):
        self.g=self.g+1
        time.sleep(1)
    def backback(self):
        self.g=self.g-1
        time.sleep(1)

    def gogo2(self,fg):
        for gh in range(0,fg):
           self.gogo()
    
    
    def backback2(self,ut):
        for gh in range(0,ut):
           self.backback()
     

    def wherecar(self):
        print self.g
        print self.name
        print self.color

hf=car()
hf.carname("will")
hf.carcolor("紅色")
hf.gogo2(10)
hf.wherecar()
hf.gogo2(5)
hf.wherecar()
hf.gogo2(3)
hf.wherecar()
hf.backback2(2)
hf.wherecar()
hf.backback2(2)
hf.wherecar()
hf.backback2(2)
hf.wherecar()
hf.backback2(2)
hf.wherecar()



