# Grupo de Maioridade

from datetime import date

q = 0
q1 = 0
for c in range(1, 8):
    i = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    a = date.today().year - i
    if a < 18:
        q += 1
    if a >= 18:
        q1 += 1
print(f'Ao todo tivemos {q1} pessoas maiores de idade')
print(f'e também tivemos {q} pessoas menores de idade')
