# Tabuada v3.0 

while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    print('-' * 40)
    if n < 0:
        break
    for c in range(0, 10):
        c += 1
        m = n * c
        print(f'{n} x {c:2} = {m}')
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')