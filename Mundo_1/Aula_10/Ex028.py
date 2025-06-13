# Jogo de Adivinhação v.1.0

import random

print('-=-' * 20)
print('voou pensar em um númeor entre 0 e 5, tente adivinhar')
print('-=-' * 20)

n1 = random.randint(0, 5)
nu = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
if n1 == nu:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(n1, nu))
    