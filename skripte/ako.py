n = int(input("Unesi n: "))

if n %2 == 0:
    print(f"{n} je paran broj")
    print("Ovo je i dalje u bloku")
if n < 50 :
    print(f"{n} je manji od 50!")
else:
    print(f"{n} je veci ili jednak 50!!!")
            
print(f"Ovo se uvijek ispisuje neovisno o broju {n}")




