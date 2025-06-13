# Jogo de Dados em Python

from random import randint
from time import sleep

jogos = dict()

for c in range(1, 5):
    jogos[f'jogador{c}'] = randint(1, 6)
print('Valores sorteados:')
sleep(1)
for k, v in jogos.items():
    print(f'  O {k} tirou {v}')
    sleep(1)

print('Ranking dos jogadores:')
njogo = sorted(jogos.items(), key=lambda x: x[1], reverse=True)
c = 0
for k, v in njogo:
    print(f'  {c + 1}º lugar: {k} com {v}')
    sleep(1)
    c += 1
   