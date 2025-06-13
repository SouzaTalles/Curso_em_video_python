# Progressão aritmétrica v2.0

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))

an = 0
c = 1

while c <= 10:
    an = p + ((c - 1) * r)
    print(an, end = ' -> ')
    c += 1
print('Acabou')