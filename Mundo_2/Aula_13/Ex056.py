# Analizador completo

si = 0
h = 0
n1 = str
q = 0

for c in range(1, 5):
    print(f'---- {c}ª PESSOA ----')
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).upper().strip()
    si += i
    if s == 'M':
        if h < i:
            h = i
            n1 = n
    if s == 'F':
        if i < 20:
            q += 1

m = si / 4
print(f'A média de idade do grupo é de {m:.2f} anos')
print(f'O homem mais velho tem {h} anos e se chama {n1}.')
print(f'Ao todo são {q} mulheres com menos de 20 anos')