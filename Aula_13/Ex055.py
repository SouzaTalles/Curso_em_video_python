# maior e menor da sequência

mp = 0
mp1 = 1000
for c in range(1, 6):
    p = float(input(f'Peso da {c}ª pessoa: '))
    if mp < p:
        mp = p
    if mp1 > p:
        mp1 = p
print(f'O maior peso lido foi de {mp}')
print(f'O menor peso lido foi de {mp1}')
