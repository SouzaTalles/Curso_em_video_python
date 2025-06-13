# Média de Aluno

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2

print(f'O aluno tirou {n1:.2f} e {n2:.2f}, com média {m:.2f}')

if m >= 7:
    print('Aluno APROVADO')
elif m >= 5 and m < 7:
    print('Aluno de RECUPERAÇÃO')
else:
    print('Aluno REPROVADO')