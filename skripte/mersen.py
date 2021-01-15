import math

n = int(input("Koliko prvih Mersenneovih brojeva želite: "))

merseni = 0

brojač = 2

while merseni < n:
    p = 2**brojač - 1
    for i in range(2, p):
        if p % i == 0:
           break
    else:
        merseni +=1
        print(f" M_{merseni} = {p}")
    brojač+= 1
            

