# Contando vogais em Tupla

p = ('banana', 'carro', 'livro', 'telefone', 'janela', 'mesa', 'cachorro', 'floresta', 'computador', 'caneta')

d = g = ''

for c in range(0, len(p)):
    print(f'Na palavra {p[c].upper()} temos ', end = '')
    d = tuple(p[c])
    for a in range (0, len(d)):
        if d[a] in 'aeiou':
            print(d[a], end = ' ')
    print()

