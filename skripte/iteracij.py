s = "Python"

iterator = iter(s)
veličina = len(s)

while veličina > 0 :
    slovo = next(iterator)
    print(slovo)
    veličina -= 1

print("Gotova petlja")

#-----------------------------

for slovo in s:
    print(slovo)

print("Gotova petlja!")
