class Kvadrat:
    
    """
    Konstruktor.
    """
  #  def __new__(cls): #zauzima mjesto u memoriji računala i čuva ju za stvoreni razred
   #     pass
    # def __init__(self,a):
    #   self.a = a

    def __init__(self, a):# nigdje eksplicitno ne postoji ova metoda, ugrađena je u python, sam je obavlja kad se kreira objekt)
        self.a = a # a u self.a je atribut, i tome atributu pridruži vrijednost "a" tj. onu koju je korisnik predao prilikom stvaranja objekta
                   # a u self.a može biti drukčije npr self.stranica = a, stvara se referenca stranica = vrij predana pri stvaranju
                   
    def calculateOpseg(self):
            return 4*self.a
    def calculatePovrsina(self):
            return self.a**2
    def __str__(self):
        return f"O = {self.calculateOpseg()}, P = {self.calculatePovrsina()}"
        
    def __lt__ (self, other):
        if self.a < other.a:
            return True
        #else: #profići ne koriste ovo
        return False
    """
    Destruktor
    """
   # def __del__(self):
    #    print("Umirem...")
        



k1 = Kvadrat(5)
print(k1.a) #poziv atributa, "a" je atribut ovom objektu

print(f"Opseg kvadrata je {k1.calculateOpseg()}")
k2 = Kvadrat(8)
opseg2 = k2.calculateOpseg()
povrsina2 = k2.calculatePovrsina()

print(f"Opseg kvadrata je {opseg2}. Površina kvadrata je {povrsina2}.")

print(k2) #ispiši na ekran ono što taj objekt zna ispisati. da bi objekt mogao nešto ispisati, mora koristiti magičnu metodu __str__

print(k1)

print(k1<k2)  #python prepoznaje znak < i pretvori zapis u k1.__lt__(k2), znači obavi funkciju bez da smo je mi expl zvali

k3 = Kvadrat(1073)

print(k3)