n = 8

while n > 0:
	print(f"{n}")
	n -= 1  
    if n % 3 == 0:
        break
    
else:
	print("Završila petlja!")
print("Ovo je izvan while-else petlje")
