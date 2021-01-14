suma = []

for i in range(0,1001):
    if i%3 == 0:
        suma.append(i)
    elif i%5 == 0:
        suma.append(i)

print(sum(suma))
