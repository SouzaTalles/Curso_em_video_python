# Progressão Aritmética

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))

an = 0

for c in range(1, 11):
    an = p + ((c - 1) * r)
    print(an, end = ' -> ')
print('Acabou')
