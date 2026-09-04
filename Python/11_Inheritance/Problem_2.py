# Animal > Pet > Dog{mtd bark()}
class Animal:
    pass
class Pet(Animal):
    pass
class Dog(Pet):
    def bark(self):
        return print("bho bhow")

a=Dog()
a.bark()    