# 2D vector and create 3D vector from it
class twoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"The vector is {self.i}i +{self.j}j")

class ThreeDvector:
    def __init__(self,i,j,k):
        # super().__init__(i,j) # for super we have to inheritate then it will work and this is another way
        self.i=i
        self.j=j
        self.k=k
    def show(self):
        print(f"The vector is {self.i}i +{self.j}j + {self.k}k")

a=twoDvector(1,2)
print(a.show())
b=ThreeDvector(1,2,3)
print(b.show())
        