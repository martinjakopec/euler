import math

suma = 0

for i in range(0,1000):
    if i % 3 == 0:
        suma += i
    elif i % 5 == 0:
        suma += i

print(suma)

