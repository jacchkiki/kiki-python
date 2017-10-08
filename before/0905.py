# -*- coding: utf-8 -*-
import time

class car:
    name=""
    g=0
    color=""

    def carname(self,ty):
        self.name="kiki"
        self.name=ty

    def carcolor(self,al):
        self.color="藍色"
        self.color=al

    def gogo(self):
        self.g=self.g+1
        time.sleep(1)
    def backback(self):
        self.g=self.g-1
        time.sleep(1)
    def gogo2(self,we):
        for gh in range(0,we):
            self.gogo()

    def backback2(self,me):
        for gh in range(0,me):
           self.backback()
    
    def wherecar(self):
        print self.color
        print self.name
        print self.g


sj=car()
sj.carname("will")
sj.carcolor("紅色")
sj.gogo2(10)
sj.gogo2(5)
sj.gogo2(3)
sj.backback2(2)
sj.backback2(2)
sj.backback2(2)
sj.backback2(2)
sj.wherecar()
