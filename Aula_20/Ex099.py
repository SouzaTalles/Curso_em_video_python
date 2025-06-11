from time import sleep

def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    if len(num) == 0:
        print('foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0')
    else:
        for v in num:
            print(f'{v} ', end = '', flush=True)
            sleep(0.5)
        print(f'foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()