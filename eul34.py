

def is_fact(x):
    
    b = int(x) + 1
    c = b 
    l = []
    
    while c > 0:
        for i in range(b):
            l.append(i)
            c -= 1
    
    j = l[1:]
    d = len(j)
    memb = iter(j)
    factus = 1
    
    while d > 0:
        factus = factus * next(memb)
        d -= 1
        
    return (int(factus))


def is_fact_dig(x):

    l = list(str(x))
    m = len(l)
    suma = 0
    k = iter(l)
    
    while m > 0:
        suma += is_fact(next(k))
        m -= 1
            
    if suma == x:
        return (x)
            
brojevi = []

for i in range(1,50000):
    if is_fact_dig(i):
        brojevi.append(i)

print(f"Zbroj brojeva čiji zbroj faktorijela znamenaka odgovara njima samima je {(sum(brojevi)-3)}.")