def leiaint(msg):
    """
    Função para validar se a entrada do usuário é um número inteiro.
    :param msg: Mensagem a ser exibida para o usuário.
    :return: Retorna um número inteiro válido.
    """
    while True:
        n = input(msg).strip()
        if n.lstrip('-+').isdigit():  # Remove o sinal antes de verificar se é número
            return int(n)
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


# Program Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o numero {n}')