# GAME: Pedra, Papel e Tesoura

from random import choice
import time

print('''Suas opções:
      [ 1 ] PEDRA
      [ 2 ] PAPEL
      [ 3 ] TESOURA''')
j = int(input('Qual é a sua jogada? '))
l = ['PEDRA', 'PAPEL', 'TESOURA']
e = choice(l)
print('JO')
time.sleep(1)
print('KEM')
time.sleep(1)
print('PO!!!')
print('-=' * 12)
print(f'computador jogou {e}')
print(f'Jogador jogou {l[j - 1]}')
print('-=' * 12)

if e == l[j - 1]:
    print('EMPATE!')
elif (e == 'PEDRA' and l[j - 1] == 'PAPEL') or (e == 'PAPEL' and l[j - 1] == 'TESOURA') or ( e == 'TESOURA' and l[j - 1] == 'PEDRA'):
    print('JOGADOR VENCEU!')
elif (e == 'PEDRA' and l[j - 1] == 'TESOURA') or (e == 'PAPEL' and l[j - 1] == 'PEDRA') or (e == 'TESOURA' and l[j - 1] == 'PAPEL'):
    print('COMPUTADOR VENCEU!')
else:
    print('\33[31m]Opção inválida. Tente novamente.\33[m]')
