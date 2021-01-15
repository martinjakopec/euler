n = input("Unesite vrijednost n: ")

if n.isdigit() != True:
    print("Niste unijeli prirodan broj!")    

else: n = int(n)
    

b = int(n + 1)

c = b

l = []

while c > 0:
    for e in range(c):
        l.append(e)
        c -= 1

print(l)

nova = l[1:b]

d = len(nova)

član = iter(nova)

umnožak = 1
print(nova)


while d > 0:
    umnožak = umnožak * next(član)
    d -= 1
    
print(umnožak)    