import math

import random

a = int(random.randint(1,50))

b = int(random.randint(1,50))

c = int(random.randint(1,50))

d = int(random.randint(1,50))

e = int(random.randint(1,50))

f = int(random.randint(1,10))

g = int(random.randint(1,10))

h = a

i = a

j = a

k = a

l = a

if b < h :
    h = b
elif c < h :
    h = c
elif d < h :
    h = d
elif e < h :
    h = e  

if b < i :
    i = b
elif c < i :
    i = c
elif d < i :
    i = d
elif e < i :
    i = e  

if b < j :
    j = b
elif c < j :
    j = c
elif d < j :
    j = d
elif e < j :
    j = e  

if b < k :
    k = b
elif c < k :
    k = c
elif d < k :
    k = d
elif e < k :
    k = e  

if b < l :
    l = b
elif c < l :
    l = c
elif d < l :
    l = d
elif e < l :
    l = e  







if f < g :
    print(f"Vaši brojevi su: {a, b, c, d, e} + {f, g}")
else:
    print(f"Vaši brojevi su: {a, b, c, d, e} + {g, f}")

print(a,b,c,d,e,f,g,h)

print(h,i,j,k,l)
    