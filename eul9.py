import math

l =[]

for a in range(1,201):
    for b in range(1,400):
        for c in range(1,500):
            
            x = ((a), (b), (c))
            if int(x[0]) < int(x[1]) and int(x[1]) < int(x[2]): 
                l.append(x)

#print(l)
pitag =[]

for e in l:
    if int(e[0]**2) + int(e[1]**2) == int(e[2]**2):
        pitag.append(e)




for n in pitag:
    if int(n[0]) + int(n[1]) + int(n[2]) == 1000:
        print(n)
        