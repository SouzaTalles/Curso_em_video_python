# Jogo da Advinhação v2.0

from random import randint

print('''Sou seu computador...
      Acabei de pensar em um nímero entre 0 e 10.
      Sará que você consegue advinhar qual foi?''')
n = randint(0, 10)
p = int(input('Qual foi o seu palpite? '))
t = 0

while n != p:
    if n > p:
        print('Mais... tente mais uma vez.')
    if n < p:
        print('Menos... tente outra vez.')
    p = int(input('Qual foi o seu palpite? '))
    t += 1
print(f'Acertou com {t + 1} tentativas. Parabéns!')
