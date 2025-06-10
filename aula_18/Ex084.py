# Lista conpostas e análise de dados

dados = list()
anali = list()
lismai = list()
lismen = list()
pe = kg = 0
pm = 9999999

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    anali.append(dados[:])
    dados.clear()
    pe += 1
    while True:
        q = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if q == "N" or q == "S":
            break
    if q == "N":
        break

print(f'Ao todo, você cadastrou {pe} pessoas.')

for p in anali:
    if p[1] > kg:
        kg = p[1]
        lismai = [p[0]]
    elif p[1] == kg:
        lismai.append(p[0])
    if p[1] < pm:
        pm = p[1]
        lismen = [p[0]]
    elif p[1] == pm:
        lismen.append(p[0])
print(f'O maior peso foi de {kg}kg. Peso de {lismai}')
print(f'O menor peso foi de {pm}kg. Peso de {lismen}')
