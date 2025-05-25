n = str(input('Digite seu nome competo: ')).strip()
print('Analisando seu nome...')
print('Seu nome competo em maúsculas é {}'.format(n.upper()))
print('Seu nome em minnúsculas é {}'.format(n.lower()))
n1 = n.split()
print("Seu nome tem ao todo {} letras".format(len(''.join(n1))))
print('Seu primeiro nome é {} e tem {} letras'.format(n1[0], len(n1[0])))

# OU

n = str(input('Digite seu nome competo: ')).strip()
print('Analisando seu nome...')
print('Seu nome competo em maúsculas é {}'.format(n.upper()))
print('Seu nome em minnúsculas é {}'.format(n.lower()))
print("Seu nome tem ao todo {} letras".format(len(n) - n.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(n.find(' ')))