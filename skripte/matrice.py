import random

m = int ( input ( " Unesi M ( broj redaka ) dimenziju matrice : " ) )
n = int ( input ( " Unesi N ( broj stupaca ) dimenziju matrice : " ) )
A = float ( input ( " Unesi realan broj A : " ) )

# list comprehension

M1 = [[ random . randint (0 ,10) for c in range ( n ) ] for r in range ( m ) ] #za svaki c(olumn) u rejndžu n, pridruži vrij 0-10
M2 = [[ random . randint (0 ,10) for c in range ( n ) ] for r in range ( m ) ]

print ( " M1 : " )

for row in range ( m ) :
    for column in range ( n ) :
        print ( f " { M1 [ row ][ column ]:3 d } " , end = " " )
    print ()

print ( " M2 : " )

for row in range ( m ) :
    for column in range ( n ) :
        print ( f " { M2 [ row ][ column ]:3 d } " , end = " " )
    print ()

# inicijalizacija matrice za zbroj
s = [[0 for c in range ( n ) ] for r in range ( m ) ]
for row in range ( m ) :
for column in range ( n ) :
s [ row ][ column ] = M1 [ row ][ column ] + M2 [ row ][ column ]
# inicijalizacija matrice za razliku
d = [[0 for c in range ( n ) ] for r in range ( m ) ]
for row in range ( m ) :
for column in range ( n ) :
d [ row ][ column ] = M1 [ row ][ column ] - M2 [ row ][ column ]
# inicijalizacija matrice za umnozak
mult = [[0 for c in range ( n ) ] for r in range ( m ) ]
for row in range ( m ) :
for column in range ( n ) :
mult [ row ][ column ] = A * M1 [ row ][ column ]
print ( " Sum : " )
for row in range ( m ) :
for column in range ( n ) :
print ( f " { s [ row ][ column ]:3 d } " , end = " " )
print ()
print ( " Difference : " )
for row in range ( m ) :
for column in range ( n ) :
print ( f " { d [ row ][ column ]:3 d } " , end = " " )
print ()
print ( " A * M1 : " )
for row in range ( m ) :
for column in range ( n ) :
print ( f " { mult [ row ][ column ]:8.2 f } " , end = " " )
print ()