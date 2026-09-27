#Tables generator

# for t in range(1,11):

#     for i in range(1,11):
#         with open("Tables.txt","a") as f:
#             f.write(f"{t} x {i} ={t*i} \n")
#     with open("Tables.txt","a") as f:
#                 f.write("------------------\n")              


def table(n):
    for i in range(1,11):
        with open("Tables.txt","a") as f:
            f.write(f"{n} x {i} ={n*i} \n")
    with open("Tables.txt","a") as f:
                f.write("------------------\n")  
table(2)                
