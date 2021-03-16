suma = 0
for a in range(1,1001):
    suma += a**a
znamenke = suma % 10**10
print(f"Zadnjih deset znamenki zbroja izraza su {znamenke}.")