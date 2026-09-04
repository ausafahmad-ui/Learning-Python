class Student:
   
    def name(self):
        print("Thanos A")

class School(Student):
    def Add(self):
        print("Hathua")
    def name(self):
        print("Hathua2")
        super().name() 
        # Student.name(d)   # direct call on the base of class refrance instead super

d=School()
d.Add()
d.name()    