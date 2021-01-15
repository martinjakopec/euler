import random

l = [random.random() for i in range(10)]

for index, e in enumerate(l, start =1):
    print(f"{index}. element je {e: .2f}")
    
    
l2 = []

for e in l:
    l2.append(e**2)
    
    
print(l2)

l2 = map(lambda x : x **2, l)

for i in l2:
    print(i)
    

def fibo(n):
    if  n == 1:
        return 0
        
    if n == 2:
        return 1
    
    return fibo(n-1) + fibo(n-2)

print(fibo(20))
