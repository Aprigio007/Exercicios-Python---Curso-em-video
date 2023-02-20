def linha(tam = 42):
	return '-' * tam


def cabecalho(txt):
	print(linha())
	print(txt.center(42))
	print(linha())

		
def menu(lista):
	c = 1	
	for item in lista:
		print(f'{c} - \033[34m{item}\033[m')
		c += 1
	print(linha())
def leiaint(msg):
	while True:
		try:
			numero = int(input(msg))
		except:
			print('\033[31mERRO! Digite um número inteiro válido!\033[m')
		else:
			return numero									