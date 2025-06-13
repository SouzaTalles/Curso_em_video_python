# Estatísticas em produtos

print('-' * 30)
print('LOJA SUPER BARATÃO'.center(30))
print('-' * 30)

t = t1 = 0
n1 = 'a'
p1 = 9999999

while True:
    n = str(input('Nome do Produto: '))
    p = float(input('Preço: R$'))
    t += p
    if p > 1000:
        t1 += 1
    if p < p1:
        p1 = p
        n1 = n
    q = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while q != "S" and q != "N":
        q = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if q == 'N':
        break
print('FIM DO PROGRAMA'.center(30, '-'))
print(f'O total da compra foi R${t:.2f}')
print(f'Temos {t1} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {n1} que custa R${p1:.2f}')
