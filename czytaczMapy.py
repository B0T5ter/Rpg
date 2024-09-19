f = open('mapa.txt', 'r').read()
f = f.split("\n")
mapaUlozenie = []
for x in f:
    mapaUlozenie.append(x.split(' '))

print(mapaUlozenie)