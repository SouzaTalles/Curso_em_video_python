# Progressão aritmétrica v3.0

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))

an = 0
c = 1
q = 0
t = 10
to = 0

while t != 0:
    to = to + t
    while c <= to:
        an = p + ((c - 1) * r)
        print(an, end = ' -> ')
        c += 1
        q += 1
    print('PAUSA')
    t = int(input('Quantos termos você quer mostrar a mais? '))
print(f'progressão finalizada com {q} termos mostrados')
