# Valores únicos em uma Lista

l = list()

while True:
    l1 = int(input('Digite um valor: '))
    if l1 in l:
        print('Valor duplicado! Não vou adicionar...')
    else:
        l.append(l1)
        print('Valor adicionado com sucesso...')
    while True:
        q = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if q == 'N' or q == 'S':
            break
    if q == 'N':
        break
print('-=' * 30)
l.sort()
print(f'Você digitou os valores {l}')