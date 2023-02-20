import random
tentativas = 0
print('Sou um computador...')
print('Acabei de pensar em um número de 0 a 10000, consegue adivinhar?')
humano = 0
numero = 0
numero = random.randint(0,10000)
while humano != numero:
	humano = int(input('Qual seu palpite?'))
	tentativas = tentativas + 1
	if humano == numero:
		print('Parabéns! Voce acertou! Eu escolhi {}.'.format(numero))
	if humano != numero:
		if humano > numero:
			print('Menos... tente denovo!')
		else:
			print('Mais... tente denovo!')	
print('Voce acertou com {} tentativas!'.format(tentativas))			