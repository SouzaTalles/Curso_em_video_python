# GAME: Pedra, Papel e Tesoura

from random import randint
import time

print('''Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
j = int(input('Qual é a sua jogada? '))
l = ['PEDRA', 'PAPEL', 'TESOURA']
e = randint(0, 2)

print('JO')
time.sleep(1)
print('KEM')
time.sleep(1)
print('PO!!!')
print('-=' * 12)
print('Computador jogou {}'.format(l[e]))
print('Jogador jogou {}'.format(l[j]))
print('-=' * 12)

if e == 0: # PEDRA
    if j == 0:
        print('EMPATE!')
    elif j == 1:
        print('JOGADOR VENCEU!')
    elif j == 2:
        print('COMPPUTADOR VENCEU!')
    else:
        print('\33[31mOpção inválida. Tente novamente.\33[m')
elif e == 1: # PAPEL
    if j == 0:
        print('COMPUTADOR VENCEU!')
    elif j == 1:
        print('EMPATE!')
    elif j == 2:
        print('JOGADOR VENCEU!')
    else:
        print('\33[31mOpção inválida. Tente novamente.\33[m')
elif e == 2: # TESOURA
    if j == 0:
        print('JOGADOR VENCEU!')
    elif j == 1:
        print('COMPUTADOR COM VENCEU!')
    elif j == 2:
        print('EMPATE!')
    else:
        print('\33[31mOpção inválida. Tente novamente.\33[m')
