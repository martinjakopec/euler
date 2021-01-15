from math import sqrt, pi

class Pravokutnik:
        
    def __init__(self, a, b):
            self.a = a
            self.b = b
        
    def calculateOpseg(self):
            return self.a*2 + self.b*2
        
    def calculatePovrsina(self):
            return self.a*self.b
        
    def calculateDijagonala(self):
            return sqrt(self.a*self.a + self.b*self.b)
        
    def calcOpKrug(self):
        if self.b <= self.a:
            return self.b*pi
        else:
            return self.a*pi
            
    def calcPoKrug(self):
        if self.b <= self.a:
            return ((self.b/2)**2)*pi
        else:
            return((self.a/2)**2)*pi
            
    def __str__(self):
            return f"Pravokutnik stranica {self.a}, {self.b} ima P = {self.calculatePovrsina()}, O = {self.calculateOpseg()}, d = {self.calculateDijagonala()}, OpKrug = {self.calcOpKrug()}"
            
            

p1 = Pravokutnik(6,4)

p2 = Pravokutnik(85, 200)


print(p1.calculateOpseg())

print(p1)
print(p2)
