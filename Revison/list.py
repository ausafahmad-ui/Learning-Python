'''
| Method      | What it does                         | Example                            |
| ----------- | ------------------------------------ | ---------------------------------- |
| `append()`  | Adds **one item** at the end         | `fruits.append("orange")`          |
| `extend()`  | Adds **multiple items** to the end   | `fruits.extend(["grape", "kiwi"])` |
| `insert()`  | Adds an item at a specific position  | `fruits.insert(1, "orange")`       |
| `remove()`  | Removes the **first matching value** | `fruits.remove("banana")`          |
| `pop()`     | Removes and **returns** an item      | `fruits.pop()`                     |
| `clear()`   | Removes all items                    | `fruits.clear()`                   |
| `index()`   | Returns the index of a value         | `fruits.index("mango")`            |
| `count()`   | Counts occurrences of a value        | `fruits.count("apple")`            |
| `sort()`    | Sorts the list                       | `fruits.sort()`                    |
| `reverse()` | Reverses the list                    | `fruits.reverse()`                 |
| `copy()`    | Creates a copy of the list           | `new = fruits.copy()`              |'''

# NOTE:List are mutable: we can change the value of list but we can't change the value of string because string is immutable.
l=[]
l.append("Apple")
l.append("Banana")  # Adds "Banana" to the end of the list
l.append("Mango")
print(l)
l.extend(["grapes"]) # Adds multiple items to the end of the list
print(l)
l.insert(1,"Orange") # Inserts "Orange" at index 1
print(l)
l.remove("Banana")  # Removes the first occurrence of "Banana"
print(l)
l.pop() # Removes and returns the last item
print(l)    
ind=l.index("Mango") # Returns the index of "Mango"
print(ind)
count=l.count("Apple") # Counts occurrences of "Apple"
print(count)
l.sort() # Sorts the list in ascending order
print(l) 
l.reverse() # Reverses the list
print(l)
l2=l.copy() # Creates a copy of the list
print(l2)                  
l.clear() # Removes all items from the list
print(l)    

tuple1 = (1, 2, 3, 4, 5)
print(tuple1[0])  # Accessing the first element of the tuple
# tuple1[0] = 10  # This will raise an error because tuples are immutable
print(tuple1)   
tuple1.count(2)  # Counts occurrences of 2 in the tuple     
tuple1.index(3)  # Returns the index of the first occurrence of 3 in the tuple
print(tuple1.count(2))  
print(tuple1.index(3))  
print   