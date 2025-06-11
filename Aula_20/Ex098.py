from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ', flush=True)
            sleep(0.5)
    if inicio > fim:
        for c in range(inicio, fim  - 1, - passo):
            print(c, end=' ', flush=True)
            sleep(0.5)
    if passo == 0:
        passo = 1
        if inicio < fim:
            for c in range(inicio, fim + 1, passo):
                print(c, end=' ', flush=True)
                sleep(0.5)
        if inicio > fim:
            for c in range(inicio, fim  - 1, - passo):
                print(c, end=' ', flush=True)
                sleep(0.5)
    if passo < 0:
        passo *= -1
        for c in range(inicio, fim  - 1, - passo):
            print(c, end=' ', flush=True)
            sleep(0.5)

# Programa Principal
print('-=' * 20)
print('Contagem de 1 a 10 de 1 em 1')
for c in range(1, 11):
    print(c, end = ' ', flush=True)
    sleep(0.5)
print()

print('-=' * 20)
print('Contagem de 10 até 0 de 2 em 2')
for c in range(10, -1, -2):
    print(c, end = ' ', flush=True) 
    sleep(0.5)
print()

print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim , passo)
