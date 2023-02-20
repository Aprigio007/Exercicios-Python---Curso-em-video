list = []
saida = False
while not saida:
	pergunta = int(input('Qual valor voce quer adicionar? '))
	if pergunta in list:
		print('Valor duplicado, não vou adicionar...')
	else:
		list.append(pergunta)
		print('Valor adicionado com sucesso...')
	pergunta2 = str(input('Quer continuar? [S/N]: ')).lower()
	if pergunta2 == 'n':
		saida = True
list.sort()		
print(f'Os valores digitados foram {list}')				