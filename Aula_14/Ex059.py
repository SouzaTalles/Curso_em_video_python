# Criando um menu de Opçoões

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0

while op != 5:
    print('''    [ 1 ] somar 
    [ 2 ] multiplicar 
    [ 3 ] maior 
    [ 4 ] novos números 
    [ 5 ] sair do programa ''')
    op = int(input('>>>>>>> Qual é a sua opção? '))
    if op == 1:
        s = n1 + n2
        print(f'A soma entre {n1} + {n2} é {s}')
        print('=-=' * 10)
    elif op == 2:
        m = n1 * n2
        print(f'O resultado de {n1} x {n2} é {m}')  
        print('=-=' * 10)
    elif op == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior é {n1}')
        else:
            print(f'Entre {n1} e {n2} o maior é {n2}')
        print('=-=' * 10)
    elif op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('=-=' * 10)
    elif op == 5:
        print('Finalizando...')
        print('=-=' * 10)
    else:
        print('Opção inválida. Tente novamente')
        print('=-=' * 10)
sleep(1)
print('fim do programa! volte sempre!')
