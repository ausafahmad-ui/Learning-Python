# Tables

def genTable(n):
    table=""
    for i in range(1,11):
        table =table+ f"{n} x {i} ={n*i}\n"
    with open(f"Tables/table_{n}.txt", "w") as f:
            f.write(table)

for count in range(1,11):
    genTable(count)          