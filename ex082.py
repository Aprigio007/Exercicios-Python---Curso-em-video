lista = []
impar = []
par = []
while True:
	pergunta = int(input('Informe um valor: '))
	lista.append(pergunta)
	pergunta2 = str(input('Quer continuar? [S/N] ')).lower()
	if pergunta2 == 'n':
		break
print(f'Na lista, tem os valores {lista}')
for c in lista:
	if c % 2 == 0:
		par.append(c)
	elif c % 2 != 0:
		impar.append(c)
print(f'Na lista, os valores ímpares são: {impar}')
print(f'Na lista, os valores par são: {par}')							