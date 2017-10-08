import time
import random

class car:
    loc=0
    name=""
    def carname(self):
        self.name="kiki"
        
    def gogo(self):
        self.loc=self.loc+1

    def backback(self):
        self.loc=self.loc-1

    def whereiscar(self):
        print self.loc
        print self.name


rt=car()
rt.carname()

d=range(0,100)

for fgw in d:
    rt.gogo()
rt.whereiscar()
