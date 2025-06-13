# Números primos

n = int(input('Digite um número: '))

d = 0

for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[33m{c}', end = ' ')
        d += 1
    else:
        print(f'\033[31m{c}', end = ' ')

print(f'\n\033[mO número {n} foi divisivel {d} vezes')

if d == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

