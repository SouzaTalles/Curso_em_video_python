#Conversor de Medidas

m = float(input('Uma distância em metros: '))
print('A medida de {}m corresponte a: '.format(m))
print('{}km'.format(m / 1000))
print('{}hm'.format(m / 100))
print('{}dam'.format(m / 10))
print('{}dm'.format(m * 10))
print('{}cm'.format(m * 100))
print('{}mm'.format(m * 1000))