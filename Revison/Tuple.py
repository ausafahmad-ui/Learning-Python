# A tuple is an immutable, ordered collection of elements in Python. Once created, you cannot modify, add, or remove elements from it.
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[0])  # Accessing the first element of the tuple      
print(my_tuple.count(2))  # Counts occurrences of 2 in the tuple
print(my_tuple.index(3))  # Returns the index of the first occurrence of 3 in the tuple
print(1 in my_tuple)  # Checks if 1 is in the tuple
print(len(my_tuple))  # Returns the length of the tuple
print(my_tuple + (6, 7))  # Concatenates two tuples
print(my_tuple * 3)  # Repeats the tuple three times
