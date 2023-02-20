from time import sleep
from random import randint
def sorteia(lista):
	cont = 0
	while cont != 5:
		n = randint(1, 10)
		lista.append(n)
		cont += 1
	print('Sorteando 5 valores:', end = ' ')
	for n in lista:
		print(n, end = ' ', flush = True,)
		sleep(0.5)
	print('PRONTO!', end = ' ')
def somaPar(lista):
	soma = 0
	for n in lista:
		if n % 2 == 0:
			soma += n
	print(f'\nSomando os valores pares de {lista} temos {soma}')							
numeros = []
sorteia(numeros)		
somaPar(numeros)

	