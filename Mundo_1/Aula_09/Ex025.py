# Procurando uma string dentro de outra

n = str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in n.lower()))
