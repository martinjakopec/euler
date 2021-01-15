n = input("Unesite vrijednost n: ")

while True:

    if n.isdigit() != True:
        print("Niste unijeli prirodan broj!")
        continue

    elif int(n) < 0:
        print("Unijeli ste broj manji od 0.")
        continue
    n = int(n)
    break
    
def fakt(n):
    umnožak = 1
    for i in range(1, n+1):
        umnožak *= i
    return umnožak
    

print(fakt(n))


def faktica(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    n *= faktica(n-1)
        return n

        