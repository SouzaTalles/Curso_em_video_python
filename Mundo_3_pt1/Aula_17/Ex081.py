# Extraindo dados de uma Lista

l = list()
n = 0

while True:
    l.append(int(input('Digite um valor: ')))
    n += 1
    while True:
        q = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if q == 'N' or q == 'S':
            break
    if q == 'N':
        break
l.sort(reverse=True)

print('-=' * 30)
print(f'Você digitou {n} elementos')
print(f'Os valores em ordem decrescente são {l}')

if 5 in l:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
