

n = int(input("Unesite vrijednost n: "))

b = int(n + 1)

l = []

iterator = iter(l)

veličina = len(l)

c = int(f"{l.min(l) + 1}")

d = int(f"{l.max(l) + 1}")

while b > 0:
    for e in range(b):
        l.append(e)
        b -= 1

print(c)
print(d)

#l = l[
# while veličina > 0:
#    član = next(iterator)
#    veličina -= 1
#    print(f"{član

#for i in range(c,d):
#    print(f"{i*(i+1)})
    
    
    
    
print(l)
