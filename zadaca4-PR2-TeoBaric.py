import re

ime = input("Unesite ime: ")
prezime = input("Unesite prezime: ")

fpmoz = "(^[a-z]{2,15})[.]([a-z]{2,15})([@]fpmoz[.]sum[.]ba$)"
sum = "^" + ime.lower()[0] + prezime.lower() + "(\d*[@]sum[.]ba$)"

while 1:
    a = input('Unesite @fpmoz.sum.ba mail: ')
    b = input('Unesite @sum.ba mail: ')
    regex1 = re.match(fpmoz, a)
    regex2 = re.match(sum, b)
    if regex1 and regex2:
        print("Email adrese uspješno unesene!")
        break
    elif not regex1:
        print("Neispravan format @fpmoz.sum.ba adrese!")
    elif not regex2:
        print("Neispravan format @sum.ba adrese!")