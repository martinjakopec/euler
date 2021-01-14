import math

zbroj = 0

def is_prime(x):
    output = True
    
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            output = False
    return output

for i in range(2,2000001):
    if is_prime(i):
        zbroj += i
        
print(zbroj)
