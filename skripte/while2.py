n = 1

while n <= 10:
    m = 1
    while m <= 10:
        print(f"{n*m:5d}", end =" ") #end =" ", zato da nas ne izbacuje u novi red
        m += 1      # uvjet da nam ne bude petlja beskonačna
    print() #print "ništa", da nas prebaci u novi red
    n += 1

print("Gotovi smo s tablicom množenja")


#--------------------------

for n in range (1,11) :
    for m in range (1,11):
        print(f"{n*m:5d}", end =" ")
    print()

