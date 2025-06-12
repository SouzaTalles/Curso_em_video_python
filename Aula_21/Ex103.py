def ficha(jog = '', gol = 0):
    """
    -> Mostra a ficha de um jogador.
    :param jog: (opcional) Nome do jogador>
    :param gol: (opcional) Número de gols marcados.
    :return: Não retorna nada, apenas mostra a ficha do jogador.
    """
    print('-' * 30)
    if jog == '':
        jog = '<desconhecido>'
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')
    print('-' * 30)


# Priograma Principal
print('-' * 30)
n = str(input('Nome do jogador: ')).capitalize() # n = nome do jogador
ng = str(input('Números de gols: ')) # ng = número de gols
ficha(n, ng)