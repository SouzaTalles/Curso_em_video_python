aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))

print(f'Nome é igual a {aluno["nome"]}').capitalize()
print(f'Média é igual a {aluno["media"]}')
if aluno['media'] >= 6:
    print('Situação é igual a aprovado')
else:
    print('Situação é igual a reprovado')
