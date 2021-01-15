tax = {
        "alkohol" : 0.25 ,
        "kava" : 0.15 ,
        "ostalo" : 0.2
}
        
products = {
            1 : { "name" : "Pivo Kar 0.5" , "price" : 12.5 , "tax" : "alkohol"},
            2 : { "name" : "Espresso" , "price" : 7 , "tax" : "kava"},
            3 : { "name" : "Macchiato" , "price" : 8 , "tax" : "kava"},
            4 : { "name" : "Americano" , "price" : 9 , "tax" : "kava"},
            5 : { "name" : "Pivo Oz 0.5" , "price" : 12.5 , "tax" : "alkohol"},
            6 : { "name" : "Coca - Cola" , "price" : 10 , "tax" : "ostalo"},
            7 : { "name" : "Fanta" , "price" : 10 , "tax" : "ostalo"},
            8 : { "name" : "Sprite" , "price" : 10 , "tax" : "ostalo"},
            9 : { "name" : "Juice" , "price" : 12.0 , "tax" : "ostalo"},
            10 : { "name" : "Kava slag" , "price" : 9, "tax" : "kava"}
}

width = 90

columns = 6

w = width // columns

while True :
    print("Sifre artikala".center(90,"="))
    print(f"{'Sifra':<{w}s}{'Artikl':^{w*2}s}")
    for code in products :
        print(f"{code:<{w}d}{products[code]['name']:<{w*2}s}")
    print("-".center(90,"-"))
    
    enter = input(f"{'Novi racun [R|r] ili Kraj rada [Q|q]: ':>{w*3}s}")
    enter = enter.lower()
    if enter == "r" :
        break
    if enter != "q" :
        continue
        
items = []

while True :
    code = input(f"{' Šifra[K|k]: ':>{w *3}s}")
    
    if code.lower() == "k":
        break

    code = int(code)

    if code not in products :
        print("Nepoznata šifra!")
        continue

    amount = int(input(f"{'Količina: ':>{w*3}s}"))
    items.append((code,amount ))
    print(f"{'Dodana stavka: ':>{w*3}s}{products[code]['name']} X {amount}")

print("Račun".center(90,"-"))
print(f"{'Šifra ':^{w}s}{'Naziv artikla ':^{w}s}{'Cijena ':^{w}s}{'Porez ':^{w}s}{'Količina ':^{w}s}{'Ukupno ':^{w}s}")

final_price = 0

final_tax = 0

for item in items :
    code = item[0]
    amount = item[1]

    prod = products[code]
    total = prod["price"]*amount
    total_tax = tax[prod["tax"]]
    final_price += total
    final_tax += total * total_tax
    
    print(f"{code:^{w}d}{prod['name']:<{w}s}{prod['price']:^{w}.2f}{total_tax:^{w}.2f}{amount:^{w}d}{total:>{w}.2f}")

print(f"{' ':{w*4}s}{'Ukupno: ':>{w}s}{final_price:>{w}.2f}")
print(f"{' ':{w*4}s}{'Porez: ':>{w}s}{final_tax:>{w}.2f}")
print(f"{' ':{w*4}s}{'Platiti: ':>{w}s}{final_price+final_tax:>{w}.2f}")
