import random

x = int(random.randint(-20,20))

b = 1

while b > 0:
    n = int(input("Pogodite broj!: "))
    
    if n > x:
        print("Vaš broj je veći od generiranog!")
    

    elif n < x:
        print("Vaš broj je manji od generiranog!")
    

    elif n == x: #tu uvjet ni ne mora biti naveden
        print("Pogodili ste broj!!!")
        break
    b += 1

print(f"Pogodili ste iz {b} pokušaja!")

print(f"Traženi broj bio je {x}!")
