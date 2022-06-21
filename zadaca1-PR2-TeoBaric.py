import random

imena = ['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko',
  'Dario', 'Mihael',
  'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan',
  'Ante', 'Ivan',
  'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip',
  'Tomislav', 'Luka', 'Ivan',
  'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana',
  'Emanuel',
  'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan',
  'Mario',
  'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan',
  'Freda', 'Kristina',
  'Josip', 'Lucija']

names = {}
ocjene = {
"Nedovoljnih" : 0,
"Dovoljnih" : 0,
"Dobrih" : 0,
"Vrlo dobrih" : 0,
"Odličnih" : 0
}

for i in imena:
 if i not in names:
  names[i] = 1
 else:
  names[i] += 1

for i in names:
 names[i] = random.randint(1, 5)
#print(names)

for i in names:
 if names[i] == 1:
  ocjene["Nedovoljnih"] += 1
 elif names[i] == 2:
  ocjene["Dovoljnih"] += 1
 elif names[i] == 3:
  ocjene["Dobrih"] += 1
 elif names[i] == 4:
  ocjene["Vrlo dobrih"] += 1
 elif names[i] == 5:
  ocjene["Odličnih"] += 1

for i in ocjene:
 print(i, ":", ocjene[i])

print("--------------------")
prosjek = (ocjene["Dovoljnih"]*2 + ocjene["Dobrih"]*3 + ocjene["Vrlo dobrih"]*4 + ocjene["Odličnih"]*5) / (ocjene["Dovoljnih"] + ocjene["Dobrih"] + ocjene["Vrlo dobrih"] + ocjene["Odličnih"])
print("Prosjek ocjena u razredu je:", round(prosjek, 2))





