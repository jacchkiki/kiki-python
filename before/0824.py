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


    def gogo2(self,skop):
        for hg in range(0,skop):
            self.gogo()

    def backback2(self,hujg):
        for hg in range(0,hujg):
            self.backback()


a=car()
a.carname("vicky")
a.gogo2(9)
a.whereiscar()

a.gogo2(5)
a.whereiscar()
            
a.backback2(9)
a.whereiscar()
