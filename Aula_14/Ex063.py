# Sequência de Fibonacci v1.0

t1 = 0
t2 = 1
c = 3

t = int(input('Quantos termos voceê quer mostrar? '))
print('~~' * 30)
print('0 -> ', end = '')
print('1 -> ', end = '')
while c <= t:
    t3 = t1 + t2
    print(f'{t3} ->', end = ' ')
    t1 = t2
    t2 = t3
    c += 1
print('fim')
print('~~' * 30)
 