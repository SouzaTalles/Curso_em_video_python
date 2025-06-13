# Detector de palíndromo 

f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
ju = ''.join(p)
i = ''

for l in range(len(ju) - 1, -1, -1):
    i += ju[l]

print(f'O inverso de {ju} é {i}')

if i == ju:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
