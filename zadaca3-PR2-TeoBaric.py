import random

imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John',
'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan',
'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']

prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez',
'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith',
'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

radnici = []

for i in range(15):
    osoba = {}
    osoba["ime"] = random.choice(imena)
    osoba["prezime"] = random.choice(prezimena)
    osoba["satnica"] = round(random.uniform(4, 6), 2)
    radnici.append(osoba)

print(radnici)
for i in radnici:
        i["tjedni_sati"] = random.randint(20, 30)

print(radnici)

obracun = []

for osoba in radnici:
    isplata = osoba["satnica"] * osoba["tjedni_sati"]
    tuples = (osoba["ime"], osoba["prezime"], isplata)
    obracun.append(tuples)

print(obracun)

zbroj = 0

for ime, prezime, isplata in obracun:
    zbroj += isplata

print("---------------------------")
prosjek = zbroj/15
print("Ukupna isplata je:", round(zbroj, 2))
print("Prosjecna isplata je:", round(prosjek, 2))

print("---------------------------")
print("IME-----PREZIME-----ISPLATA")
for ime, prezime, isplata in obracun:
    if isplata > prosjek:
        print(ime, "-", prezime, "-", round(isplata))


