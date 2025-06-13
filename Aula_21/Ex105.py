# Analisando e gerando Dicionários 

def notas(*no, sit=False):
    """
    notas(*no, sit=False)
        -> Função para analisar notas e situações de vários alunos.
        :param no: (float) Notas dos alunos.
        :param sit: (bool) (opconal) Se True, retorna a situação dos alunos.
        :return: um dicionário com várias informações sobre a situação dos alunos.
    """
    d = dict()
    d['total'] = len(no) # Total de notas
    d['maior'] = max(no) # maior nota
    d['menor'] = min(no) # menor nota
    d['média'] = sum(no) / len(no) # média dos alunos 
    if sit:
        if d['média'] >= 7:
            d['situação'] = 'BOA'
        elif d['média'] >= 5:
            d['situação'] = 'RAZOÁVEL'
        else:
            d['situação'] = 'RUIM'
    print('-' * 30)
    return d


#  Programa Principal
resp = notas(3, 9, 5, 3, 3, sit=True)
print(resp)
# help(notas)  # Exibe a documentação da função notas
# resp = notas(3, 9, 5, 3, 3)
