from datetime import datetime
ano = datetime.today().year
nascimento = int(input('Qual seu nascimento?'))
idade = ano - nascimento
cima = idade - 18
baixo = 18 - idade
if idade > 18:
	print('Voce devia ter se alistado a {} ano atras!'.format(cima))	
elif idade < 18:
	print('Relaxa, ainda falta {} anos para voce se alistar!'.format(baixo))
elif idade == 18:
	print('Ja está na hora de se alistar!')								