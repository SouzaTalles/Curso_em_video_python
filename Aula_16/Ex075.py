# Análise de dados em uma Tupla

n = int(input('Digite um número: '))
n1 = int(input('Digite outro número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Digite o útimo número: '))

nu = (n, n1, n2, n3)

print(f'Você digitou os valores: {nu}')

n9 = n4 = nn = 0

for c in range(0, len(nu)): # Pderia ter usado o .count()
    if nu[c] == 9:
        n9 += 1
    if nu[c] == 3: # poderia ter usado o index()
        n4 = c
        nn += 1

print(f'O valor 9 apareceu {n9} vezes')
if nn >= 1:
    print(f'O valor 3 apareceu na {n4 + 1}ª posição')
else:
    print(f'O valor 3 apareceu em nenhuma posição')

print('os valores pares digitados foram', end = ' ')

for c in range(0, len(nu)):
    if nu[c] % 2 == 0:
        print(nu[c], end = ' ')
        