d = float(input('Qual é a diatância daa sua viagem? '))

if d <= 200:
    p = d * 0.50
    print('E o preço da sua passagem será de R${:.2f}'.format(p))
else:
    p = d * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(p))
print('Tenha uma boa viagem!')

# OU

d = float(input('Qual é a diatância daa sua viagem? '))
p = d * 0.50 if d <=200 else d * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(p))
