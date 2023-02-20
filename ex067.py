cont = 0
while True:
	pergunta = int(input('Quer ver a tabuada de qual valor? '))
	if pergunta <= -1:
		print('Finalizando programa...')
		break
	for c in range(1, 11):
		print(f'{pergunta} X {c} = {pergunta * c}')	
	