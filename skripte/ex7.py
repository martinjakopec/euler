x1 = float(input("Unesite točku x1: "))
x2 = float(input("Unesite točku x2: "))
y1 = float(input("Unesite točku y1: "))
y2 = float(input("Unesite točku y2: "))

c = ((x2) - (x1))
d = ((y2) - (y1))
e = ((d)/(c))
g = ((x1*e) + y1)



if c == 0 :
    print("Ne mogu dijeliti s nulom!")
    
print(f"y = {e} * x + {g}")

