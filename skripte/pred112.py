n = int(input("Unesi ocjenu: "))

if n == 1 :
    print("nedovoljan")
if n == 2 :
    print("dovoljan")
if n == 3 :
    print("dobar")
if n == 4 :
    print("vrlo dobar")
if n == 5 :
    print("izvrstan")
    
if n < 1 or n > 5 :
    print("Unesite ocjenu od 1 do 5!")
