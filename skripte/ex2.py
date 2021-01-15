n = input("Unesite riječ ili rečenicu: ")

a = n [:]

b = a.upper()

c = b.replace(" ","")

if c == c[-1: :-1] :
    print(f"Rečenica '{a}' je palindrom!")
else:
    print(f"Rečenica '{a}' nije palindrom!")
