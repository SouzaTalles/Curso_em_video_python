jog = dict()
gols = list()
g = 0

jog['nome'] = str(input('Nome do Jogador: ')).capitalize()
q = int(input(f'Quantas partidas {jog['nome']} jogou? '))
for c in range(0, q):
    go= int(input(f'Quantos gols na partida {c}? '))
    gols.append(go)
    g += go
jog['gols'] = gols[:]
jog['total'] = g
print('-=' * 30)
print(jog)
print('-=' * 30)

for k, v in jog.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)

print(f'O jogador {jog['nome']} jogou {q} partidas.')
for c, v in enumerate(jog['gols']):
    print(f'  => Na partida {c}, fez {v} gols.')
print(f'Foi um total de {jog['total']} gols.')
