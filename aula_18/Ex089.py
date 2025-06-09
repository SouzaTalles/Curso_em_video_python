l1 = list()
l2 = list()
l3 = list()
m = 0

while True:
    l2.append(str(input('Nome: ')).strip().capitalize())
    n1 = float(input('Nota 1: '))
    l3.append(n1)
    n2 = float(input('Nota 2: '))
    l3.append(n2)
    l2.append(l3[:])
    l1.append(l2[:])
    l2.clear()
    l3.clear()
    while True:
        q = str(input('Quer continuar? [S/N] ')).upper().strip()
        if q == 'S' or q == 'N':
            break
    if q == 'N':
        break
print('-=' * 25)
print('NO. NOME             MÉDIA')
print('-' * 30)
for c,v  in enumerate(l1):
    m = (v[1][0] + v[1][1]) / 2
    print(f'{c:<4}{v[0]:<18}{m:.1f}')
print('-' * 30)

while True:
    a = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if a == 999:
        break
    print(f'Notas de {l1[a][0]} são {l1[a][1]}')
    print('-' * 30)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
    
