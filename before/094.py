# -*- coding: utf-8 -*-
import time

class car:
    color=""
    name=""
    j=0

    
    def carname(self):
        self.name="kiki"


    def carcolor(self):
        self.color="藍色"

    def gogo(self):
        self.j=self.j+1

    def backback(self):
        self.j=self.j-1

    

    def gogo2(self,we):
        for gh in range(0,we):
            self.gogo()

    def backback2(self,me):
        for gh in range(0,me):
           self.backback()
    
    def wherecar(self):
        print self.color
        print self.name
        print self.j

kj=car()
kj.carname()
kj.carcolor()
kj.gogo2(3)
kj.wherecar()

        
