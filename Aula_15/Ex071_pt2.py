print('=' * 30)
print('BANCO'.center(30))
print('=' * 30)

v = int(input('Que valor você quer sacar? R$'))
t = v
c = 50
totced = 0
while True:
    if t >= c:
        t -= c
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        elif c == 1:
            c = 0
        totced = 0
        if t == 0:
            break
print('=' * 30)
print('volte sempre ao BANCO! Tenha um bom dia!')