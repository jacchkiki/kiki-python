import time

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

    def backback2(self,gd):
        for dg in range(0,gd):
            self.backback()

    def gogo2(self,jg):
        for hs in range(0,jg):
            self.gogo()

    def whereiscar(self):
        print self.p
        print self.name


aj=car()
aj.carname()
aj.gogo2(15)
aj.whereiscar()
