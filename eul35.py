import math
from collections import deque
def is_prime(x):
    prim = True
    a = int(math.sqrt(x)+1) 
    for i in range(2,a):
        if x % i == 0:
            prim = False
            break
    if prim:
        return True
def is_circular(x):
    if not is_prime(x):
        return False
    y = list(str(x))
    B = deque(y[:])
    L = []
    for e in range(len(B)):
        a = list(B)
        f = "".join([str(i) for i in a])
        g = int(f)
        if is_prime(g):
            L.append(g)
            B.rotate()
    if len(L) == len(y):
        return True
circular = [e for e in range(2, 1000000) if is_circular(e)]
print(circular)
print(len(circular))