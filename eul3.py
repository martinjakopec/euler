broj = 600851475143

import math

def prim(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
    
for e in range(2, broj):
    if prim(e):
        if broj % e == 0:
            print(e)
            
    

