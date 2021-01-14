a = 0
b = 1 
c = 0

suma = 0

while c <= 4000000 :
    c = a + b
    a, b = b, c
    
    if c%2 == 0:
        suma += c

print(suma)