pessoas = list()
temp = list()
maior = menor = 0
while True:
	temp.append(str(input('Nome: ')))
	temp.append(float(input('Peso: ')))
	if len(pessoas) == 0:
		maior = menor = temp[1]
	else:
		if temp[1] > maior:
			maior = temp[1]
		if temp[1] < menor:
			menor = temp[1]		
	pessoas.append(temp[:])
	temp.clear()
	pergunta = str(input('Quer continuar? [S/N] '))
	if pergunta in 'Nn':
		break
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso registrado foi de {maior}KG, nas pessoas:', end = ' ')
for p in pessoas:
	if p[1] == maior:
		print(f'{p[0]}|', end = ' ')
		
print(f'\nO menor peso registrado foi de {menor}KG, nas pessoas:', end = ' ')
for p in pessoas:
	if p[1] == menor:
		print(f'{p[0]}|')	