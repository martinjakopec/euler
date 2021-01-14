found = 0
counter = 2
while found < 10:
# lista djeljitelja
    divisors = []
    for i in range (1 , counter) :
# ako je djeljitelj , dodaj ga u listu
        if counter % i == 0:
            divisors.append(i)
# provjeri zbroj
    suma = sum(divisors)
    if suma == counter :
        found += 1
        print(f"Nadjen je savrsen broj {counter}. Njegovi djeljitelji su {divisors}.")
    counter += 1
 
 