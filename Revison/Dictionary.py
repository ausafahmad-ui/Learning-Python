'''
| Method         | Specification / Purpose                                                     | Example                                  |
| -------------- | --------------------------------------------------------------------------- | ---------------------------------------- |
| `get()`        | Returns value for a key without raising error if key doesn't exist          | `student.get("name")`                    |
| `keys()`       | Returns all keys                                                            | `student.keys()`                         |
| `values()`     | Returns all values                                                          | `student.values()`                       |
| `items()`      | Returns key-value pairs                                                     | `student.items()`                        |
| `update()`     | Adds or updates key-value pairs                                             | `student.update({"age": 26})`            |
| `pop()`        | Removes a specified key and returns its value                               | `student.pop("age")`                     |
| `popitem()`    | Removes and returns the last inserted key-value pair                        | `student.popitem()`                      |
| `setdefault()` | Returns value if key exists; otherwise inserts the key with a default value | `student.setdefault("country", "India")` |
| `clear()`      | Removes all key-value pairs                                                 | `student.clear()`                        |
| `copy()`       | Creates a shallow copy of the dictionary                                    | `new = student.copy()`                   |
| `fromkeys()`   | Creates a new dictionary from given keys with the same default value        | `dict.fromkeys(["a","b"], 0)`            |'''



d ={"marks":90,
    "gender":"male",
    "Loc":"Delhi"}

print(d.get("marks")) 
print(d.keys())
print(d.items())
print(d.values())
d.update({"marks":100})
print(d.get("marks"))
print(d.pop("gender"))
print(d.items())
print(d.popitem())
print(d.items())
print(d.update({"Country":"India"}))
print(d.items())