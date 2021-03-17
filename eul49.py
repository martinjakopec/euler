from math import sqrt
def is_prime(x):
	for i in range(2, int(sqrt(x))+1):
		if x%i == 0:
			return False
	return True
    
for i in range(1000,10000):
    if is_prime(i):
        j = i + 3330
        if is_prime(j):
            k = j + 3330
            if is_prime(k):
                a = list(str(i))
                b = list(str(j))
                c = list(str(k))
                if sorted(a) == sorted(b) and sorted(b) == sorted(c):
                    print(f"Traženi niz brojeva je {i, j, k}.")