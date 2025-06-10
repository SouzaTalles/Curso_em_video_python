jog = dict()
gols = list()
totjog = list()
g = 0

while True:
    jog['nome'] = str(input('Nome do Jogador: ')).capitalize()
    g = 0
    q = int(input(f'Quantas partidas {jog['nome']} jogou? '))
    for c in range(0, q):
        go= int(input(f'Quantos gols na partida {c}? '))
        gols.append(go)
        g += go
    jog['gols'] = gols[:]
    jog['total'] = g
    totjog.append(jog.copy())
    gols.clear()
    while True:
        q = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if q in 'SN':
            break
    if q == 'N':
        break

print(f'{"COD.":<4}{"NOME":<12}{"GOLS":<15}{"TOTAL":<5}')
print('-' * 40)
for c, v in enumerate(totjog): 
    print(f"{c:<4}{v['nome']:<12}{str(v['gols']):<15}{v['total']:<5}")
print('-' * 40)

# for k, v in jog.items():
#     print(f'O campo {k} tem o valor {v}.')
# print('-=' * 30)

while True:
    a = int(input('Mostrar dados de qual jogador? (999 interrompe): '))
    if a == 999:
        break
    if a >= len(totjog):
        print(f'ERRO! Não existe jogador com código {a}.')
    else:
        print(f'-- Levantamento do jogador {totjog[a]["nome"]}:')
        for c, v in enumerate(totjog[a]['gols']):
            print(f'  => Na partida {c}, fez {v} gols.')
print('<<< VOLTE SEMPRE >>>')  
