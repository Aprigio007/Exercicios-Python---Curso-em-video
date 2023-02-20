dicionario = {}
dicionario['Nome'] = input('Nome: ')
nascimento = int(input('Ano de Nascimento: '))
dicionario['Idade'] = 2023 - nascimento
dicionario['Carteira de Trabalho'] = int(input('Carteira de trabalho (0 não tem): '))	
if dicionario['Carteira de Trabalho'] != 0:
	dicionario['Ano de Contratação'] = int(input('Ano de contratação: '))
	dicionario['Salario'] = float(input('Salário: '))
	dicionario['Aposentadoria'] = dicionario['Ano de Contratação'] + 35 - nascimento	
print('-=' * 30)	
for k, i in dicionario.items():
	print(f'   - {k} tem o valor {i}')	
		