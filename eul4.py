def palindrom(x):
    x = str(x)
    if x[:] == x[-1: :-1]:
        return True
    return False

l =[]

#for i in range(10000, 1000000):
#    if palindrom(i):
#        print(i)
#        
for a in range(100, 1000):
    for b in range(100, 1000):
        c = a*b
        if palindrom(c):
            l.append(c)

print(max(l))