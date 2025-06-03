ti = th = tm = 0

while True:
    print('-' * 20)
    print(f'{"CADASTRE UMA PESSOA":^20}')
    print('-' * 20)
    i = int(input('Idade: '))
    if i >= 18:
        ti += 1
    s = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while s != 'M' and s != 'F':
        s = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-' * 20)
    if s == 'M':
        th += 1
    if s == 'F' and i < 20:
        tm += 1
    q = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while q != 'S' and q != 'N':
        q = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if q == 'N':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {ti}')
print(f'Ao todo temos {th} homens cadastrados')
print(f'E temos {tm} mulheres com menos de 20 anos')
