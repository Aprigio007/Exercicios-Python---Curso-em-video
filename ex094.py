pessoas = {}
dados = {}
contador = 0
media = 0
soma_de_idades = 0
contador2 = 1
saida = False
while not saida:
	dados['nome'] = input('Nome: ')
	sexo = str(input('Sexo [M/F]: ')).upper()
	if sexo != 'M' and sexo != 'F':
		while True:
			sexo = str(input('ERRO! Digite apenas M ou F!\nSexo [M/F]: ')).upper()
			if sexo == 'M' or sexo == 'F':
				break
	dados['sexo'] = sexo			
	idade = int(input('Idade: '))
	dados['idade'] = idade
	contador += 1
	pessoas[f'pessoas{contador}'] = dados.copy()
	pergunta = str(input('Quer continuar? [S/N] ')).upper()
	if pergunta == 'N':
		break
	elif pergunta != 'S' and pergunta != 'N':
		while not saida:
			pergunta = str(input('ERRO! Digite apenas S ou N\nQuer continuar? [S/N] ')).upper()
			if pergunta == 'S':
				break
			elif pergunta == 'N':
				saida = True													
print(f'Ao todo foram {len(pessoas)} pessoas cadastradas')
for c, p in pessoas.items():
	soma_de_idades += pessoas[f'{c}']['idade']
	media = soma_de_idades / len(pessoas)
print('A média de idades é de {:.2f}'.format(media))
print('As mulheres cadastradas foram', end = ' ')
print()	
for c, p in pessoas.items():
	if pessoas[f'{c}']['sexo'] == 'F':
		print(pessoas[f'{c}']['nome'], end = ' ')
	else:
		print('Não existe mulheres cadastradas!')
		break	
print('\nLista de pessoas que estão acima da média: ')
for c, p in pessoas.items():
	if pessoas[f'{c}']['idade'] > media:
		for g, v in pessoas[f'{c}'].items():
			print(f'{g} = {v}', end  = ' ')																				