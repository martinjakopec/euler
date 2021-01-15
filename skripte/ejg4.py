import random

brojevi = []

for i in range(5):
    brojevi.append(random.randint(0,50))    

brojevi.sort()
print(brojevi)
