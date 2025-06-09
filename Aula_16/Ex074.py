# Maior e menor valores em tuplas

from random import randint

nu = tuple(randint(1, 10) for _ in range(5))
print(f'Os valores sorteados foram: {nu}')

m = 0
me = 20

for c in range(0, len(nu)):
    if nu[c] > m:
        m = nu[c]
    if nu[c] < me:
        me = nu[c]
print(f'O maior valor sorteado foi {m}')
print(f'O menor valor sorteado foi {me}')
