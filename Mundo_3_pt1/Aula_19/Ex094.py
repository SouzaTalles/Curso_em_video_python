# Unindo dicionários e listas

pes = dict()
dados = list()

while True:
    pes['nome'] = str(input('Nome: ')).capitalize()
    pes['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while pes['sexo'] not in 'MF':
        pes['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    pes['idade'] = int(input('Idade: '))
    dados.append(pes.copy())
    while True:
        q = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if q in 'SN':
            break
    if q == 'N':
        break
print('-=' * 30)

print(f'O grupo tem {len(dados)} pessoas.')

m = f = s = 0
for c in dados:
    s += c['idade']
    f +=1
m = s / f
print(f'- A média de idade é de {m:.2f} anos.')

print('- As mulheres cadastradas foram: ', end='')
for c in dados:
    if c['sexo'] == 'F':
        print(f"{c['nome']}", end=' ')
print()

print('- Lista das pessoas que estão acima da média:')
for c in dados:
    if c['idade'] > m:
        print(f'Nome = {c["nome"]}; Sexo = {c["sexo"]}; Idade = {c["idade"]};')
print('<<< ENCERRADO >>>')
