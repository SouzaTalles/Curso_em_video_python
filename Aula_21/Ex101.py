# Funções para votação

def voto(nas):
    from datetime import date
    idade = date.now().year - nas
    if idade < 18:
        v = 'NÃO VOTA'
    elif idade < 65:
        v = 'VOTO OBRIGATÓRIO'
    else:
        v = 'VOTO OPCIONAL' 
    return idade, v


# Codigo principal
lis = []
print('-=' * 20)
a = int(input("Em que ano você nasceu? "))
lis = voto(a)
print(f'Com {lis[0]} anos: {lis[1]}')