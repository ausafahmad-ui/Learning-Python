n : int = 5
name: str = "Ausaf"

def sum(a:int,b:int) ->int:
    return a + b
print(sum(3,3))

#for advance type we have to import 
from typing import List,Tuple,Union 

num : List[int]=[1,2,45]
person : Tuple[str,int] =("ausaf",90)
source :dict[str,int] ={"age":90,"Salary":10000}
identifier : Union[str,int] ="ID1234"
