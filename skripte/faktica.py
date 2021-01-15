n = int(input("Unesite broj n: "))

l = [range(1,n)]

#j = i * (i+1)

#for i in range(1,n) :
#    j = i * (i+1)
#    print(j)

print(l)

z = len(l)

i = 1

while z > 0:
    i *= i+1
    z -= 1
    print(i)

