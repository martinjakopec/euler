import random

l = []

for i in range(100):
	l.append(random.randint(-10,10))
	
print(l)

l = []

for i in range (100):
	for j in range (90):
		if i > j:
			l.append((i,j))
			
print(l)

#može i ovako:

l = [(i,j) for i in range (100) for j in range (90) if i > j]


