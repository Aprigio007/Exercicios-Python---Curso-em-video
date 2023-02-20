palavras = ('Python', 'Programar', 'Estudar')
print('VERIFICADOR DE VOGAIS')
for p in palavras:
	print(f'\nNa palavra {p} temos: ', end = ' ')
	for vogal in p:
		if vogal in 'aeiou':
			print(vogal, end = ' ')