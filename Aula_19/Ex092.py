from datetime import date

dados = dict()

dados['nome'] = str(input('Nome: ')).capitalize()
a = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - a
dados['ctps'] = int(input('Cateira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['contratação'] + 35 - a
print(dados)
print('-=' * 30)

for k, v in dados.items():
    print(f'{k} tem o valor {v}')
    