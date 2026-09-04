'''
| Method                   | Purpose                                              | Example                     |
| ------------------------ | ---------------------------------------------------- | --------------------------- |
| `add()`                  | Adds one element                                     | `numbers.add(5)`            |
| `update()`               | Adds multiple elements                               | `numbers.update([5, 6])`    |
| `remove()`               | Removes an element; error if not found               | `numbers.remove(3)`         |
| `discard()`              | Removes an element; no error if not found            | `numbers.discard(3)`        |
| `pop()`                  | Removes and returns an arbitrary element             | `numbers.pop()`             |
| `clear()`                | Removes all elements                                 | `numbers.clear()`           |
| `copy()`                 | Creates a copy of the set                            | `new = numbers.copy()`      |
| `union()`                | Combines elements from sets                          | `a.union(b)`                |
| `intersection()`         | Returns common elements                              | `a.intersection(b)`         |
| `difference()`           | Returns elements only in first set                   | `a.difference(b)`           |
| `symmetric_difference()` | Returns elements present in either set, but not both | `a.symmetric_difference(b)` |
| `issubset()`             | Checks whether one set is contained in another       | `a.issubset(b)`             |
| `issuperset()`           | Checks whether one set contains another              | `a.issuperset(b)`           |
| `isdisjoint()`           | Checks whether two sets have no common elements      | `a.isdisjoint(b)`           |

'''

s={1,4,"3","Adeeb"}
print(s)
print(type(s))
s.add([907,"p"])
s.update([20,"hh"])
print(s)