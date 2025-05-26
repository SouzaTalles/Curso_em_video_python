s = float(input('Qual o salário do funcionárrio? R$ '))

if s > 1250:
    novo = s * 1.1
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(s, novo))
else:
    novo = s * 1.15
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(s, novo))

# Na percentagem pode ser usado (s * 10 / 100) + s
# ou (s * 15 / 100) + s