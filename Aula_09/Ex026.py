# Primeira e última ocorrência de uma string

f = str(input('Digite uma frase: ')).strip()
print('A lrtra A aparece {} vezes na frase.'. format(f.lower().count('a')))
print('a primeiroa letra A apareceu na posição {}'.format(f.lower().find('a') + 1))
print('A última letra A apareceu na posição {}'.format(f.lower().rfind('a') + 1))
