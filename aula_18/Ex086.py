# Matriz em Python

lis1 = []

for c in range(0, 3):
    for f in range(0, 3):
        lis1.append(int(input(f'Digite um valor para [{c}, {f}]: ')))
        
print('-=' * 20)

print(f'[ {lis1[0]} ] [ {lis1[1]} ] [ {lis1[2]} ]')
print(f'[ {lis1[3]} ] [ {lis1[4]} ] [ {lis1[5]} ]')
print(f'[ {lis1[6]} ] [ {lis1[7]} ] [ {lis1[8]} ]')
