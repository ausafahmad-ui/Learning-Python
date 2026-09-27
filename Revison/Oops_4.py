class Car:
    wheel=4
    def __init__(self,company,cc):
        self.company=company
        self.cc=cc
    @staticmethod
    def greet():
        print("Hello! welcome to the world of Cars")
    def info(self):
        print(f"This is {self.company} and its car wheel {self.wheel} of {self.cc}")

c= Car("Audi",2000)
c.greet()
c.info()        