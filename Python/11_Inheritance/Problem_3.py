# Employee class > salary mtd and increament mtd
class Employee:
   Salary=500 
   Increament=20
   @property
   def SalaryAfterIncreament(self):
      return round(self.Salary+(self.Salary*self.Increament)/100)
   @SalaryAfterIncreament.setter
   def SalaryAfterIncreament(self,value):
      self.Increament=((value-self.Salary)/self.Salary)*100
     
e=Employee()   
# print(e.SalaryAfterIncreament())
e.SalaryAfterIncreament=1000
print(e.Increament)