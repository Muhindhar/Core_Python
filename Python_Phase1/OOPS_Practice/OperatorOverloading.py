class complex:
    def __init__(self,r,i):
        self.real = r
        self.img = i
    def __add__(self, sec):
        r = self.real + sec.real
        i = self.img + sec.img
        return complex(r,i)
    def __str__(self):
        return str(self.real)+'+'+str(self.img)+'I'
c1 = complex(5,2)
c2 = complex(2,4)
print("sum : ",c1,c2)