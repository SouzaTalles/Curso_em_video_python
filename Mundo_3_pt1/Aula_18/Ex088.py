#   Palpites para a Mega Sena

from random import sample
from time import sleep

numega = list()

print('-=' * 20)
print('JOGA NA MEGA SENA'.center(40))
print('-=' * 20)

q = int(input('Qauntos jogos você quer que sorteie? '))
print(f'-=-=-= SORTEANDO {q} JOGOS -=-=-=')

for c in range(0, q):
    jogo = sorted(sample(range(1, 60), 6))
    numega.append(jogo)

for c, v in enumerate(numega, 1):
    print(f'Jogo {c}: {v}')
    sleep(1)
print('-=-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=-=')
