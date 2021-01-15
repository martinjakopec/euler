n = input("Unesite cijeli broj veći ili jednak 0: ")

if n.isdigit() != True and int(n) < 0:
    print("Niste unijeli cijeli broj!")

else:
    m = int(n)

a = 0
b = 1 

while m > 0 :
    c = a + b
    a, b = b, c
    print(c)
    m -= 1


# for i in range(n):
#   print