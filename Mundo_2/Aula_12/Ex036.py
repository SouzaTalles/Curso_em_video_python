# Aprovando empréstimo

v = float(input('Qual o valor da casa? R$'))
s = float(input('Qaul o seu salário? R$'))
a = int(input('Em quantos anos você preetende pagar? '))
p = v / (a * 12)
po = s * 30 / 100

print(f'Para pagar uma casa de {v:.2f} em {a} anos a prestação será de R${p:.2f}!')

if p <= po:
    print('Empréstimo aprovado!')
else: 
    print('Empréstimo negado!')
