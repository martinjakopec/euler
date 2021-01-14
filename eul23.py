import math

def is_abun(x):
    l = []
    for i in range(1, x):
        if x%i == 0:
            l.append(i)
    if sum(l) > x:
        return True
    

ab = []

for e in range(1,28124):
    if is_abun(e):
        ab.append(e)
print(ab)
zbrojevi = []

for e in ab:
    for f in ab:
        zbrojevi.append(e+f)

brojevi= list(range(1,28124))

s1 = set(ab)
s2 = set(zbrojevi)
s3 = set(brojevi)
#print(s1)
#print(s2)

s4 = set(s1.union(s2))
#print(s4)

s5 = set(s3 - s1)

fin = list(s5)
#print(fin)
c = sum(fin) + 50

print("test")

print(c)

