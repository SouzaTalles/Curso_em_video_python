from random import choice
p1 = input('Primeiro aluno: ')
p2 = input('Segundo aluno: ')
p3 = input('terceiro aluno: ')
p4 = input('Quarto aluno: ')
alunos = [p1, p2, p3, p4]
sorteio = choice(alunos)
print('O aluno escolhido foi {}!'.format(sorteio))
