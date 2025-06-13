# maior e menor valores

c = "S"
q = s = g = 0
f = 999
while c != 'N':
    n = int(input('Digite um número: '))
    c = str(input('Quer continuar? [S/N] ')).strip().upper()
    q += 1
    s += n
    if n > g:
        g = n
    if n < f:
        f = n
me = s / q
print(f'Você digitou {q} números e a média foi {me}')
print(f'O maior valor foi {g} e o menor foi 2')