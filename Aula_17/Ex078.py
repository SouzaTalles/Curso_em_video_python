l = list()
m = 0
me = 999999

for c in range(0, 5):
    l.append(int(input('Digite um valor: ')))
print('=-' * 30)
print(f'Você digitou os valores {l}')

for v in l:
   if m < v:
       m = v
print(f'O maior valor digitado foi {m} nas posições ', end = '')
for i, v in enumerate(l):
    if v == m:
        print(f'{i}', end = '... ')
print()

for b in l:
    if me > b:
        me = b
print(f'O menor valor digitado foi {me} nas posições ', end = '')
for i, v in enumerate(l):
    if v == me:
        print(f'{i}', end = ' ...')
