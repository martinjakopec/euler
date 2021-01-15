n = int(input("Unesi cijeli broj: "))

prim = True

for i in range(2,n) :
	if n % i == 0:
		prim = False
		break
		
if prim == True: # može i bez "== True", jer već sam "prim" je ispitivanje je li true
	print(f"Broj {n} je prost!")
else:
	print(f"Broj {n} nije prost!")
	