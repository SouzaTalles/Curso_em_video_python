# Validando expressões matemáticas()

l = list(input('Digite a expressão: '))
e = d = 0
for c in l:
    if c == '(':
        e += 1
    if c == ')':
        d += 1

if e == d:
    print('Sua expressão está correta!')
else:
    print('Sua Expressão está errada!')
    