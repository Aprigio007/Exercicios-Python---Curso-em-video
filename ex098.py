from time import sleep
def contador(i, f, p):
	print(f'Contando de {i} a {f} indo de {p} em {p}: ')
	cont = i
	if i <= f:
		while cont <= f:
			print(f'{cont}', end = ' ', flush = True)
			sleep(0.5)
			cont += p
		print()
	elif i >= f:
		cont = i
		while cont >= f:
			print(f'{cont}', end = ' ', flush = True)
			sleep(0.5)
			cont -= p
		print()						
contador(1, 10, 1)
contador(10, 0, 2)	
inicio = int(input('Inicio: '))
Fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, Fim, passo)	