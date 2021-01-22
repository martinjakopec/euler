#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
#For example, 2143 is a 4-digit pandigital and is also prime.
#What is the largest n-digit pandigital prime that exists?
from math import sqrt

def is_prime(x):
    for i in range(2, int(sqrt(x))+1):
        if x%i == 0:
            return False
    return True

def is_pandig(x):
    if not is_prime(x):
        return False
    digits = [int(e) for e in str(x)]
    checklist = [i for i in range(1, len(digits)+1)]
    if sorted(digits) == checklist:
        return True
    
numbers = [i for i in range(7652414) if is_pandig(i)]
print(f"There are {len(numbers)} pandigital primes, and the largest pandigital prime that exists is {max(numbers)}.")
