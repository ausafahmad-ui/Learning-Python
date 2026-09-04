#NOTE:Problem 2 add static method of Greet()

import math
class Calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        return self.n*self.n
    def cube(self):
        return self.n*self.n*self.n
    def root(self):
        return math.sqrt(self.n)
    @staticmethod
    def dummy():
        print("Hello Users")
s=Calculator(64)
print(s.square())    
print(s.cube())    
print(s.root())   
s.dummy() 