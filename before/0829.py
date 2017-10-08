import time

class car:
    r=0
    name=""

    def carname(self):
        self.name="kiki"
        
    def gogo(self):
        self.r=+1
        
    def backback(self):
        self.r=-1

    def gogo2(self,jk):
        self.r=+1
        for aa in range(0,jk):
            self.gogo()    

    def backback2(self,hd):
        self.r=-1
        for sd in range(0,hd):
            self.backback()

    def wearscar(self):
        print self.r
        print self.name
        

ca=car()
ca.carname()
ca.gogo2(7)
ca.wearscar()
