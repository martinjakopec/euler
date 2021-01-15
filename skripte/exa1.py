import random

m = int(input("Unesi M ( broj redaka ) dimenziju matrice : "))
n = int ( input ( " Unesi N ( broj stupaca ) dimenziju matrice : " ) )
A = float ( input ( " Unesi realan broj A : " ) )

# list comprehension

M1 = [[ random . randint (0 ,10) for c in range ( n ) ] for r in range ( m ) ] #za svaki c(olumn) u rejndžu n, pridruži vrij 0-10
M2 = [[ random . randint (0 ,10) for c in range ( n ) ] for r in range ( m ) ]

print("M1 : ")

for row in range(m) :
    for column in range(n) :
        print(f"{M1[row][column]:3d}" , end =" ")
    print()

print("M2 : ")

for row in range(m) :
    for column in range(n) :
        print(f"{M2[row][column]:3d}" , end =" ")
    print()
    
