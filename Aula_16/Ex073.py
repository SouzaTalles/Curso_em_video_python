# Tuplas com times de Futebol

times = ('Flamengo', 'Cruzeiro', 'Red Bull Bragantino', 'Palmeiras', 'Fluminense', 'Botafogo', 'Bahia', 'Mirassol', 'Atlético-MG', 'Ceará', 'Corinthians', 'Grêmio', 'São Paulo', 'Internacional', 'Fortaleza', 'Goiás', 'Vasco', 'Cuiabá', 'América-MG', 'Coritiba')

print(f'Lista do Brasileirão: {times}')
print('-=' * 40)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 40)
print(f'Os 4 útimoss são: {times[16:]}')
print('-=' * 40)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 40)

for c, d in enumerate(times):
    if d == 'São Paulo':
        print(f'O São Paulo está na {c + 1}ª posição')

#  print(f'O São Paulo está na {times.index("São Paulo") + 1}ª posição)