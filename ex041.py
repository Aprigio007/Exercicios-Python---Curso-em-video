nascimento = int(input('Qual o ano de seu nascimento? '))
idade = 2023 - nascimento
if  idade <=9 and idade >= 0:
	print('Voce e um nadador mirim!')
elif idade > 10 and idade <= 14:
	print('Voce é um nadador infantil!')	
elif idade > 15 and idade <= 19:
	print('Voce é um nadador junior!')
elif idade == 20:
	print('Voce é um nadador senior')
elif idade >= 21:
	print('Voce é um nadador master')
elif idade > -1 and idade > 110:
	print('Opção inválida, tente novamente!')			 					