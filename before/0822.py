import time
import random

class car:
    loc=0
    name=""
    def carname(self,fc):
        self.name=fc
        
    def gogo(self):
        self.loc=self.loc+1

    def backback(self):
        self.loc=self.loc-1

    def whereiscar(self):
        print self.name
        print self.loc



rt=car()
rt.carname("will")
rt.gogo()
rt.gogo()
rt.gogo()
rt.backback()
rt.whereiscar()


b=car()
b.carname("kiki")
b.gogo()
b.gogo()
b.gogo()
b.backback()
b.whereiscar()

c=car()
c.carname("xuan")
c.gogo()
c.gogo()
c.gogo()
c.backback()
c.whereiscar()
