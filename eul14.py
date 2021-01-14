

def operacija(n):
    rezultat = int(n)
    l = [int(n)]
    
    while rezultat > 1:
    
        if rezultat%2 == 0:
            rezultat = rezultat/2
            l.append(rezultat)
        else:
            rezultat = 3*rezultat + 1
            l.append(rezultat)
        
    
    return int(len(l))

#print(operacija(13))
#print((len(operacija(13))))

rječnik ={}

for i in range(3,1000001):
    rječnik[int(i)] = [operacija(i)]

#print(rječnik)


for k, v in rječnik.items():
    if int(v[0]) == 525:
        print(f"Najveći broj izraza u lancu, 525, ima broj {k}.")
        
print("gotovo")