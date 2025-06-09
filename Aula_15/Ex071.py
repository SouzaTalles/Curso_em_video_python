print('=' * 30)
print('BANCO'.center(30))
print('=' * 30)

v = int(input('Que valor você quer sacar? R$'))

q50 = q20 = q10 = q1 = 0


if v >= 50:
   q50 = v // 50
   v = v % 50
if v < 50 and v >= 20:
    q20 = v // 20
    v = v % 20
if v < 20 and v >= 10:
    q10 = v // 10
    v = v % 10
if v < 10 and v >= 1:
    q1 = v // 1
    v = v % 1

if q50 >= 1:
    print(f'Total de {q50} cédulas de R$50')
if q20 >= 1:
    print(f'Total de {q20} cédulas de R$20')
if q10 >= 1:
    print(f'Total de {q10} cédulas de R$10')
if q1 >= 1:
    print(f'Total de {q1} cédulas de R$1')
print('=' * 30)
print('volte sempre ao BANCO! Tenha um bom dia!')
