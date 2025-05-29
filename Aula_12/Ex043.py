#Índice de Massa Corporal (IMC)

p = float(input('Qual o seu peso? (kg) '))
a = float(input('Qual a sua altura? (m) '))
imc = p / a ** 2
print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print('você está ABAIXO do peso ideal.')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está com OBSIDADE.')
else:
    print('Você está com OBESIDADE MÓRBIDA.')
