n = input("Unesite cijeli broj: ")

if not n.isdigit () :
    print("Niste unijeli cijeli broj!")

m = str(n)

o = str(len(m))

print(m[-1])

print("Broj" + (m) + "ima" + (o)+ "znamenaka")
