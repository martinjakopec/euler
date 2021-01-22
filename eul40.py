#Champernowne's constant
#An irrational decimal fraction is created by concatenating the positive integers
#               0.123456789101112131415161718192021...
#If dn represents the nth digit of the fractional part, find the value of the following expression:
#               d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

champ_cons = ""
for i in range(1000000):
    champ_cons += str(i)
d = 1
result = 1
while d <= 1000000:
    result *= int(champ_cons[d])
    d *= 10
print(f"The value of the above mentioned expression is {result}.")