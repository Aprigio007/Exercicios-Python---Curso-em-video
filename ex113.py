def leiaint(msg):
	numero = 0
	while True:
		try:
			numero = int(input('Digite um numero inteiro: '))
		except:
			print('\033[31mERRO! Digite um número inteiro válido!\033[m')
		else:
			print(f'Voce digitou o número {numero}')
			break	
def leiafloat(msg):
	while True:
		try:
			numero = float(input(msg))
		except:
			print('\033[31mERRO! Digite um número real válido!\033[m')
		else:
			print(f'Voce digitou o número {numero}')
			break
leiafloat('Digire um numero')											