mulhermaisnova = 0
nomevelho = ' '
homemmaisvelho = ' '
somaidade = 0
for p in range(1, 5):
	print('---------- {}ª PESSOA----------'.format(p))
	nomes = str(input('Qual o nome da {}ª?'.format(p)))
	idades = int(input('Qual a idade da {}ª? '.format(p)))
	sexos = str(input('Qual o sexo da {}ª [M/F]: '.format(p)))
	if p == 1 and sexos == 'M':
		homemmaisvelho =+ idades
		nomevelho = nomes		
	elif p != 1 and sexos == 'M':
		homemmaisvelho = homemmaisvelho =+ idades
		nomevelho = nomes			
	somaidade = somaidade + idades
	if p == 1 and sexos == 'F' and idades < 20:
		mulhermaisnova = mulhermaisnova + 1
	elif p != 1 and sexos == 'F' and idades < 20:
		mulhermaisnova = mulhermaisnova + 1	
media = somaidade / 4
print('A média das idades é de {}.'.format(media))
print('O nome do homem mais velho é {}.'.format(nomevelho))
print('Existem {} mulheres com menos de 20 anos.'.format(mulhermaisnova))			