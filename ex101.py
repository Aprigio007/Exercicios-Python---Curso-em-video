
def voto(nascimento):
	import datetime
	ano = datetime.datetime.now().year
	idade = ano - nascimento
	if idade < 16:
		return f'Com {idade} anos, Voto NEGADO.'
	elif idade >= 16 and idade < 18:
		return f'Com {idade} anos, Voto OPCIONAL.'
	else:
		return f'Com {idade} anos, Voto OBRIGATÓRIO.'
print('=' * 50)
ano = int(input('Ano de Nascimento: '))
print(voto(ano))			