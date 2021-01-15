bruto1 = float(input("Unesi bruto1 iznos [kn]: "))

mio1_stopa = 0.15 #1. stup mirovinskog
mio2_stopa = 0.05 #2. stup mirovinskog
porez = 0.2 #porez u RH
prirez_zagreb = 0.18 #prirez u Gradu Zagrebu
neoporeziv_iznos = 4000.00 #neoporeziv iznos bez poreznih olakšica
zdravstveno_stopa = 0.165 #stopa bruto1 place za zdrav. osiguranje

mio1 = mio1_stopa * bruto1
mio2 = mio2_stopa * bruto1

X1 = bruto1 - mio1 - mio2

X2 = X1 - neoporeziv_iznos

X3 = porez * X2

X4 = prirez_zagreb * X3

neto = bruto1 - mio1 - mio2 - X3 - X4

zdravstveno = zdravstveno_stopa * bruto1

bruto2 = bruto1 + zdravstveno

#odluka: platna lista se ispisuje na veličinu od 90 znakova
#platna lista će imati 6 stupaca, dakle polje iznosi 15 znakova
#|-w-|-w-|-w-|-w-|-w-|-w-|
#sirina = w * broj stupaca

#sirina platne liste (ovo se moze mijenjati)
sirina = 90

#broj stupaca u platnoj listi
stupaca = 6
#sirina jednog stupca
w = sirina // stupaca 

#ispisivanje naslova
print("PLATNA LISTA".center(sirina,"_"))

#primijeti: zbroj w-ova u retku mora biti 6 jer je 6 stupaca

#ispisivanje bruto plaće
print(f"{' ':{w*5}}{'Bruto':^{w}}")
print(f"{' ':{w*5}}{bruto1:>{w}.2f}")

#ispisivanje mirovinskih doprinosa
print(f"{'Doprinosi iz':<{w*3}s}{'Stopa':^{w}s}{'Osnovica':^{w}s}{'Iznos':^{w}s}")
print(f"{'MIO1':<{w}s}{'Doprinos za MIO I stup':<{w*2}s}{mio1_stopa*100:>{w}.2f}{bruto1:>{w}.2f}{mio1:>{w}.2f}")
print(f"{'MIO2':<{w}s}{'Doprinos za MIO II stup':<{w*2}s}{mio2_stopa*100:>{w}.2f}{bruto1:>{w}.2f}{mio2:>{w}.2f}")
print(f"{' ':{w*5}}{mio1+mio2:>{w}.2f}")

#ispisivanje poreza
print(f"{'Porez':<{w*2}s}{'Odbitak':^{w}s}{'Stopa':^{w}s}{'Osnovica':^{w}s}{'Iznos':^{w}s}")
print(f"{'POR':<{w}s}{'Porez':<{w}s}{neoporeziv_iznos:>{w}.2f}{porez*100:>{w}.2f}{X2:>{w}.2f}{X3:>{w}.2f}")

#ispisivanje prireza
print(f"{'Prirez':<{w*3}s}{'Stopa':^{w}s}{'Osnovica':^{w}s}{'Iznos':^{w}s}")
print(f"{'PRIR':<{w}s}{'Prirez - Grad Zagreb':<{w*2}s}{prirez_zagreb*100:>{w}.2f}{X3:>{w}.2f}{X4:>{w}.2f}")

#ispis neto plaće
print(f"{' ':{w*5}}{'Neto':^{w}}")
print(f"{' ':{w*5}}{neto:>{w}.2f}")

#ispis zdravstvenih doprinosa
print(f"{'Doprinosi na':<{w*3}s}{'Stopa':^{w}s}{'Osnovica':^{w}s}{'Iznos':^{w}s}")
print(f"{'ZDRAV':<{w}s}{'Doprinos za zdrav. osiguranje':<{w*2}s}{zdravstveno_stopa*100:>{w}.2f}{bruto1:>{w}.2f}{zdravstveno:>{w}.2f}")
print(f"{' ':{w*5}}{0.165 * bruto1:>{w}.2f}")

#ispis ukupnog troška plaće
print(f"{' ':{w*5}}{'Trošak plaće':^{w}}")
print(f"{' ':{w*5}}{bruto2:>{w}.2f}")
