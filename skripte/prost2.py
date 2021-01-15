n = int(input("Koliko prostih brojeva želiš: "))

ispitujem = 2

brojač = 0

l = []

while brojač < n:
    
    prim = True
    for i in range(2,ispitujem) :
        if ispitujem % i == 0:
            prim = False
            break
            
    if prim == True: # može i bez "== True", jer već sam "prim" je ispitivanje je li true
        brojač += 1
        l.append(ispitujem)
    #    print(f"Broj {ispitujem} je prost!")  
    #if brojač == n: #1. oblik rješenja, ali bolje je gore u while
    #    break
    ispitujem += 1

print(max(l))