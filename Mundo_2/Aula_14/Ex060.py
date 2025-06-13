# Cálculo do Fatorial

n = int(input("Digite um número para calcular seu fatorial: "))
c = n
m = 1

print(f'Calculando {n}! = ', end = ' ')

while c > 0:
    print(f'{c} ', end = '') 
    print('x ' if c > 1 else '= ', end = '')
    m *= c
    c -= 1
print(f'{m}')
