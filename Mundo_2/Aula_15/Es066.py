# Vários números com flag

s = q = 0

while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    s += n
    q += 1
print(f'A soma dos {q} valores foi {s}')
