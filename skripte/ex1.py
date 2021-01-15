a = float(input("Unesi a: "))
b = float(input("Unesi b: "))
c = float(input("Unesi c: "))

t = float((-b)/(a*2))
p = float((b*b)-(a*c*4))
q = float((((b*b)-(a*c*4))**0.5)/(a*2))

if p < 0 :
    print("Imaginarni brojevi!! Ne znam riješiti!")
    
x1 = float(t-q)
x2 = float(t+q)



print(str("Rješenje x1 = ") + str(x1))

print(str("Rješenje x2 = ") + str(x2))





