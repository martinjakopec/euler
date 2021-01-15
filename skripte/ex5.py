a = float(input("Unesi prvi operator: "))
b = input("Unesi operand ") # dozvoljeni su +,-,* i /
c = float(input("Unesi drugi operator: "))

if b == "+" :
    print(f"{a} + {c} = {a + c}")
    
if b == "-" :
    print(f"{a} - {c} = {a - c}")
    
if b == "*" :
    print(f"{a} - {c} = {a * c}")
    
if b == "/" :
    print(f"{a} / {c} = {a / c}")