import random

x = str("atcg") # može se i s rječnikom, gdje su baze ključevi s pridodanim vrijednostima, pa ih se tako iterira

# x ={
#   A : 0
#   T : 1
#   C : 2
#   G : 3
#}
#
#
#
#

baze = list(x)

print(baze[1])

gen = []

while True:
        for i in range(0,100):
            gen.append(baze[random.randint(0,3)])
        break

print(gen)
print(len(gen))

            



#n = input("Unesite rečenicu: ")

lista = list(gen)

print(lista)

rječnik = {}

for element in lista:
    if element in rječnik:
        rječnik[element] += 1
    else:
        rječnik[element] = 1
        
for znak, broj in rječnik.items():
    print(f"Znak {znak} se pojavljuje {broj} puta.")
    
najčešći = max(rječnik.values())

for znak in rječnik:
    if rječnik[znak] == najčešći:
        print(f"Najviše puta, ({najčešći}) pojavio se znak {znak}.")

print(rječnik)

y = str(gen)

z = y.replace(" ","")
w = z.replace("'","")
q = w.replace(",","")


print(f"Sekvenca gena glasi: {q}")