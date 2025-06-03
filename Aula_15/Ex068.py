from random import randint

v = a = 0

while True:
    print('=-' * 20)
    print('VAMOS JOGAR PAR OUM ÍMPAR')
    print('=-' * 20)
    n = int(input('Diga um valor: '))
    j = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    c = randint(1, 10)
    s = n + c
    print('-' * 20)
    if s % 2 == 0:
        print(f'Você jogou {n} e o computador {c}. total de {s} DEU PAR')
    else:
        print(f'Você jogou {n} e o computador {c}. total de {s} DEU ÍMPAR')
    print('-' * 20)
    if s % 2 == 0:
        if j == 'P':
            print('Você VENCEU!!')
            v += 1
            a = 0
        else: 
            print('Você PERDEU!')
            a = 1
    if s % 2 != 0:
        if j == "I":
            print('Você VENCEU')
            v += 1
            a = 0
        else:
            print('você PERDEU')
            a = 1
    if a == 1:
        break
    print('Vamos jogar novamente...')
print(f'GAMER OVER! Você venceu {v} vezez.')
