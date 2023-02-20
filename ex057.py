sexo = ' '
while sexo != 'M' and sexo != 'F':
	sexo = str(input('Digite seu sexo [M/F]: '))
	if sexo == 'M' or sexo == 'F':
		print('Dados aceitos!')
	if sexo != 'M' and sexo != 'F':
		print('Dados Negados! Tente novamente!')					