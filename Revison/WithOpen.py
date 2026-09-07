# Read the Poem file and validate the given word that present in that or not
'''
| Method          | Output type                      | Example                | Perform
| --------------- | -------------------------------- | ---------------------- | -------------
| `read()`        | **String (`str`)**               | `"Hello\nWorld"`       | → Whole file
| `readline()`    | **String (`str`)**               | `"Hello\n"`            | → One line
| `readlines()`   | **List (`list`)**                | `["Hello\n", "World"]` | → All lines as a list
| `for line in f` | **String (`str`) per iteration** | `"Hello\n"`            | → One line at a time
'''


with open("Poem.txt", "r") as f:
    poem=f.read()

word="jack"
if word in poem.lower().split():
    print("yes")
else:
    print("No")