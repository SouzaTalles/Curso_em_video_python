# Alistamento Militar

from datetime import date

i = int(input('Ano de nascimento: '))
a = date.today().year - i
at = date.today().year
print(f'Quem nassceu em {i} tem {a} anos em {at}.')

if a < 18:
    p = 18 - a
    print(f'Ainda faltam {p} anos para o alistameto.')
    print(f'Seu alistamento será em {at + p}.')
elif a > 18:
    p = a - 18
    print(f'Você deveria ter se alistado há {p} anos.')
else:
    print('Você deve se alistar IMEDIATAMENTE!')
    