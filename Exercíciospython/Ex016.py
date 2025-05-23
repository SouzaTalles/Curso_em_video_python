from math import trunc
n = float(input('digite um número: '))
print('O número digitado foi {} e a sua parte inteira é {}'.format(n, trunc(n)))

# or

n = float(input('digite um número: '))
print('O número digitado foi {} e a sua parte inteira é {}'.format(n, int(n)))
