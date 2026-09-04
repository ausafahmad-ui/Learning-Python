#Farenhit to celcius

def f_to_c(f):
    c=5*(f-32)/9
    return round(c,2)

f=int(input("Your temp: "))
print(f"{f_to_c(f)} degree celcius")