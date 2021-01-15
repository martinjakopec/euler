import random

import math

n = int(input("Unesite broj elemenata liste: "))

mn = int(input("Unesite najnižu vrijednost liste (minimum): "))

mx = int(input("Unesite najvišu vrijednost liste (maximum): "))

l = [mn, mx]

a = n - 2

while a > 0:
    l.append(random.randint(mn,mx))
    a -= 1
print(l)

print(mn)

print(mx)

d = len(l)

c = d

zbroj = 0

i = iter(l)

while c > 0:
    zbroj += next(i)
    c -=1

mi = zbroj/d
print(zbroj)
print(mi)

sig = 0

j = iter(l)

f = d

while f > 0:
    sig += ((next(j) - mi)**2)
    f -= 1
    
print(sig)
x = int((sig/(n-1)))

y = math.sqrt(x)

print(y)

g = l

for q in range(len(g)):
    for w in range(q+1, len(g)):
        if g[q] > g[w]:
            g[q], g[w] = g[w], g[q]
            
print(g)

v = int(len(g)/2)

if len(g) % 2 != 0:
    print(g[v])
else:
    med = int((g[v] + g[v-1])/2)
    print(med)


for z in g:
    if z > 1.5*(med):
        print(z)

print(l)
