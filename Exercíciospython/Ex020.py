from random import shuffle
p1 = str(input('Primeiro aluno: '))
p2 = str(input('Segundo aluno: '))
p3 = str(input('Terceiro aluno: '))
p4 = str(input('Quarto aluno: '))
alunos = [p1, p2, p3, p4]
shuffle(alunos)
print('A ordem de apresentaçao será:')
print(alunos)
