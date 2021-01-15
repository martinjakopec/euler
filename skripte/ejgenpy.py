import random

n = 1

m = 0

a = int(random.randint(1,50))

b = int(random.randint(1,50))

c = int(random.randint(1,50))

d = int(random.randint(1,50))

e = int(random.randint(1,50))

f = int(random.randint(1,10))

g = int(random.randint(1,10))

if f < g :
    print(f"Vaši brojevi su: {a, b, c, d, e} + {f, g}")
else:
    print(f"Vaši brojevi su: {a, b, c, d, e} + {g, f}")

print(a,b,c,d,e,f,g)    