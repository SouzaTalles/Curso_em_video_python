# Primeiro e último nome de uma pessoa

n = str(input('Digite seu nome completo: ')).strip()
n = n.split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n) - 1]))
