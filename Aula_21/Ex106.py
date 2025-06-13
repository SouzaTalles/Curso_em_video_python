# Interactive helping system in Python

from time import sleep

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'{msg:^{tam}}')
    print('~' * tam)
    

while True:
    print('\033[44m', end='')  # Fundo azul
    escreva('SISTEMA DE AJUDA PyHELP')
    print('\033[m', end='')   # Reset de cores
    comando = input('Fução ou Biblioteca > ')
    if comando.upper() == 'FIM':
        escreva('\033[41mATÉ LOGO!\033[m')
        break
    else:
        print('\033[42;37m', end='')  # Fundo verde, texto branco
        escreva(f'Acessando o manual do comando {comando}')
        print('\033[m', end='')  # Reset de cores
        sleep(1)
    print('\033[7;30;40m', end='')  # Inverso, letra preta, fundo preto
    help(comando)
    print('\033[m', end='')  # Reset
    sleep(1) 
