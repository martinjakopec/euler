from math import sqrt

def is_prime(x):
	for i in range(2, int(sqrt(x))+1):
		if x%i == 0:
			return False
	return True

def is_trunc(x):
    if not is_prime(x):
        return False
    a = (str(x))
    if not is_prime(int(a[0])):
        return False
    if not is_prime(int(a[-1])):
        return False
    if int(a[0]) == 1 :
        return False
    if int(a[-1]) == 1:
        return False
    b = a
    h = len(a)
    while h > 0:
        for i in range(h):
            c = b[i:]
            d = b[0:i]
            if d == '':
                d = 3
            if not is_prime(int(c)):
                return False
            if not is_prime(int(d)):
                return False
        h -= 1
    return True
L = [e for e in range(22, 1000000) if is_trunc(e)]

print(L)
print(sum(L))
print(len(L))