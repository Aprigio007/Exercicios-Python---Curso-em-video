def notas(*notas, sit = True):
	"""
	A função 'notas' recebe uma quantidade indefinida de notas e retorna um dicionário com informações sobre as notas inseridas. O dicionário inclui o total de notas, a menor nota, a maior nota e a média das notas. Além disso, é possível optar por incluir a situação do aluno (Ruim, Razoável ou Boa), com base na média. Caso o argumento 'sit' seja False, a situação não é incluída no dicionário retornado.
	"""
	dicionario = {}
	dicionario['total'] = len(notas)
	dicionario['menor'] = min(notas)
	dicionario['maior'] = max(notas)
	dicionario['média'] = sum(notas) / len(notas)
	if dicionario['média'] < 5:
		dicionario['situação'] = 'Ruim'
	elif dicionario['média'] <= 6 and dicionario['média'] >= 5:
		dicionario['situação'] = 'Razoável'
	elif dicionario['média'] > 7:
		dicionario['situação'] = 'Boa'	
	if sit == False:
		del dicionario['situação']
	return dicionario			
help(notas)	