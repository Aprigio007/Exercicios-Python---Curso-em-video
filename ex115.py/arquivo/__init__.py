import uteis


def verificararquivo(arquivo):
	try:
		a = open(arquivo, 'rt')
		a.close()
	except:
		return False
	else:
		return True	

						
def criararquivo(arquivo):
	try:
		a = open(arquivo, 'wt+')
		a.close()
	except:
		print(f'Houve um erro ao criar o arquivo {arquivo}')
	else:
		print(f'Arquivo {arquivo} Criado com sucesso')


def lerarquivo(arquivo):
	try:
		a = open(arquivo, 'rt')	
	except:
		print('Não foi possivel acessar o arquivo')
	else:
		print(uteis.cabecalho('CADASTRAMENTO DE PESSOAS'))
		try:
			for linha in a:
				dado = linha.split(';')
				dado[1] = dado[1].replace('\n', ' ')
				print(f'{dado[0]: <30}{dado[1]: <3}')
		except:
			print('Houve um erro ao ler os dados')	
def cadastrar(arq, nome = 'desconhecido', idade = 0):
	try:
		a = open(arq, 'at')
	except:
		print('Houve um erro ao abrir o arquivo!')
	else:
		try:
			a.write(f'{nome};{idade:} anos\n')
		except:
			print('Ocorreu um erro ao escrever o arquivo')
		else:
			print('Registrado com sucesso!')
		finally:
			a.close()																