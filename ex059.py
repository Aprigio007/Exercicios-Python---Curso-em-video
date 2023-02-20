import time
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
sair = False 
while not sair:
	pergunta = int(input('Oque deseja fazer? \n [1] somar \n [2] subtrair \n [3] multiplicar \n [4] dividir \n [5] maior \n [6] novos números \n [7] sair do programa \n'))
	if pergunta == 1:
		print(f'{n1} + {n2} = {n1 + n2}')
	if pergunta == 2:
		print(f'{n1} - {n2} = {n1 - n2}')
	if pergunta == 3:
		print(f'{n1} x {n2} = {n1 * n2}')
	if pergunta == 4:
		if n2 == 0:
			print('Impossivel dividir por zero, tente novamente!')
		elif n2 != 0:
			print(f'{n1} ÷ {n2} = {n1 / n2}')	
	if pergunta == 5:
		if n1 > n2:
			print('{} é maior que {}.'.format(n1, n2))
		elif n2 > n1:
			print('{} é maior que {}.'.format(n2,n1))
		elif n1 == n2:
			print('Os dois valores são iguais!')	
	if pergunta == 6:
		n1 = float(input('Informe o primeiro valor: '))
		n2 = float(input('infotme o segundo valor: '))
	if pergunta == 7:
		print('Finalizando...')
		time.sleep(1)
		sair = True
	if pergunta >= 8:
		print('Opcão inválida. Tente novamente!')
														