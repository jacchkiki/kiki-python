import time,os

class car:
    name=""
    p=0
    color=""

    def carname(self):
        self.name="kiki"

    def gogo(self):
        self.p=self.p+1

    def backback(self):
        self.p=self.p-1

    def gogo2(self,df):
        for gg in range(0,df):
            self.gogo()

    def backback2(self,tf):
        for gg in range(0,tf):
            self.backback()

    def whereiscar(self):
        print self.p
        print self.name


gj=car()
gj.carname()
gj.gogo2(15)
gj.whereiscar()
