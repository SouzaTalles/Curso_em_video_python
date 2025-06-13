# Um print especial

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'{msg:^{tam}}')
    print('~' * tam)


# Programa Principal
escreva('Ola, Mundo!')
escreva('Curso de Python no YouTube')