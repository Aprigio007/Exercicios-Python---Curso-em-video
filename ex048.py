cont = 0
total = 0
for c in range(0, 501, 3):
	if c % 2 != 0 and c % 3 == 0:
		cont = cont + 1
		total += c
print('A soma de todos os {} valores é correspondente a {}.'.format(cont, total))							