#NOTE: Program is for complex number and add to overloaded mtd of addition and multiplication
# '''Real part
# ac−bd
# (1×9)−(3×8)
# 9−24=−15
# Imaginary part
# ad+bc
# (1×8)+(3×9)
# 8+27=35'''


class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i 

    def add(self,c2):
        return Complex(self.r+ c2.r,self.i+c2.i)#yaha direct return kroge sum to complex add to complex kaise karoge to tuple banega
    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i        #Ye complex ka formula hota hai tension ni lena hai 
        imag = self.r * c2.i + self.i * c2.r        
        return Complex(real, imag)



    def __str__(self):
        return f"{self.r} + {self.i}i"
c1=Complex(1,3)
c2=Complex(9,8)   
print(c1.add(c2))  # yaha maine c1 obj refr per add() function ko call mkiya fir usme add(c2) c2 obj refrance dala
print(c1*c2)# direct c1 and c2 ko multiply * operned se call kiya