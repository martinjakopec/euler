def is_cut(x, y):
    l = list(str(x))
    k = list(str(y))
    if x/y >1:
        return False
    elif x == y:
        return False
    elif l[0] == l[1]:
        return False
    elif k[0] == k[1]:
        return False
    elif str(0) in l:
        return False
    elif str(0) in k:
        return False
    for i in l:
        for j in k:
            if i == j:
                l.remove(i)
                k.remove(j)
                l[0] = int(l[0])
                k[0] = int(k[0])
                if x/y == int(sum(l))/int(sum(k)):
                    return True
  
    
    
    

print(is_cut(49, 98))

l =[]
for i in range(10,100):
    for j in range(10,100):
        if is_cut(i,j):
            l.append(i)
            l.append(j)
            

print(l)
x = list(l[0: :2])
y = list(l[1: :2])
brojnik = 1
nazivnik = 1

for i in x:
    brojnik *= i 
for i in y:
    nazivnik *= i

print(f"{brojnik}/{nazivnik} = {brojnik/nazivnik}")