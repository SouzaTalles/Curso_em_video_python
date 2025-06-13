# Tratando vários valores v1.0

c = s = n = 0
while c != 999:
    c = int(input('Digite um número [999 para parar]: '))
    if c != 999:
        s += c
        n += 1
print(f'Você digitou {n} números e a soma entre eles foi {s}.')
