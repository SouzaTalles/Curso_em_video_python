# Função para Fatorial

def fatorial(num, re=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param re: (opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    print('-' * 20)
    for c in range(num, 0, -1):
        f *= c
        if re:
            print(f'{c} ', end='')
            if c > 1:
                print('x ', end='')
            else:
                print('= ', end=' ')
    return f
    

# Programa Principal
print(fatorial(5, True))
