#NOTE:Make class calculator and create three methods of sq,cube and root

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
    
s=Calculator(64)
print(s.square())    
print(s.cube())    
print(s.root())    