def ispis(n):
    i = 0
    while i < n:
        yield i
        i += 1

n = int(input("Unesite broj: "))
for i in ispis(n):
    print(i)