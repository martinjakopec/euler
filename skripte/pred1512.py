class A:

    def ispisi(self):
        print("Ja sam iz A")
        

a = A()
a.ispisi()  # A.__dict__["ispisi"](a) <-- tako python gleda na liniju a.ispisi



class Osoba:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    
    def __str__(self):
        return str(self.kwargs)


o1 = Osoba()
o2 = Osoba(ime = "Karlo")

o3 = Osoba(oib = 1234, ime = "Darja")

print(o1)
print(o2)
print(o3)
