a = input("Unesite matematički izraz i znakom jednakosti ga zatvorite: ")

b = a[ : ]

b = b.replace(" ","")

c = len(b)

iterator = iter(b)

while c > 0 :
    član = next(iterator)
    print(član)
    c -= 1

if "+" in b :
    d = b[0,"+"]
    e = b["+", ]
    
    print(f"{d} + {e} = {d + e}")
    
