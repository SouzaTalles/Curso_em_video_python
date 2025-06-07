# Dividindo valores em várias listas

l = list()
l1 = list()
l2 = list()

while True:
    l.append(int(input('Digite um valor: ')))
    while True:
        q = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if q == 'N' or q == 'S':
            break
    if q == 'N':
        break

for c in l:
    if c % 2 == 0:
        l1.append(c)
    else:
        l2.append(c)
print(f'Alista completa é {l}')
print(f'A lista de pares {l1}')
print(f'A lista de ímpares é {l2}')