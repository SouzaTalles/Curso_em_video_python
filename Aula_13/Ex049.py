# Tabuada v.2.0

n = int(input('Digite um número para ver sua tabuada: '))

n1 = 0

for c in range(1, 11):
    n1 = n * c
    print(f'{n} x {c:2} = {n1:2}')

#OU
print(" ")

for c in range(1, 11):
    print(f'{n} x {c:2} = {n * c}')
