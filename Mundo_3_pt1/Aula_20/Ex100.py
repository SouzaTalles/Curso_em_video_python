# Funções para sortear e somar

from random import choice
from time import sleep

def sorteio():
    numeros = list()
    print('Sorteando 5 valores da lista: ', end='')
    for _ in range(5):
        num = choice(range(1, 10))
        numeros.append(num)
        print(num, end=' ', flush=True)
        sleep(0.5)
    print()
    return numeros


def somapar(numeros):
    print(f'Somando os valores pares de {numeros},', end=' ')
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'temos {soma}')


# Programa Principal
numeros = sorteio()
somapar(numeros)
