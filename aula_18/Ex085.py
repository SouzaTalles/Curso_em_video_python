# Listas com pares e ímpares

lispar = list()
lisimp = list()
listo = list()

for c in range(1, 8):
    v = int(input(f'Digite o {c}ª valor: '))
    if v % 2 == 0:
        lispar.append(v)
    elif v % 2 != 0:
        lisimp.append(v)
lispar.sort()
lisimp.sort()
listo.append(lispar)
listo.append(lisimp)

print(f'Os número digitados separados em listas de ímpares e pares são {listo}')
