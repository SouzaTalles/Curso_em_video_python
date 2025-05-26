km = float(input('Qual a velocidade do carro? '))
if km > 80:
    multa = (km - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um dom dia! Dirija com segurança!')