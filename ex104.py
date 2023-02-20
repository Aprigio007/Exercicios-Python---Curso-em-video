def leiaint(msg):
	saida = False
	numero = 0
	while not saida:
		numero = input(f'{msg}')
		if numero.isdigit():
			print(f'Voce digitou o número {numero}')
			break
		else:
			print('ERRO! Digite apenas um número inteiro!')		
a = leiaint('Digite um número: ')			
			