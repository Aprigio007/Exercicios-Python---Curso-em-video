import random
cont = 0
vezes_ganha = 0
while True:
	numero = int(input('Qual numero vai jogar? '))
	pergunta = str(input('Par ou ímpar? [P/I]')).lower()
	maquina = random.randint(0, 10)
	soma = maquina + numero
	if pergunta == 'p':
		if soma % 2 == 0:
			print(f'Parabens! Eu escolhi {maquina} e voce venceu')
			vezes_ganha += 1
		if soma % 2 != 0:
			print(f'Eu ganhei! Escolhi {maquina}. vamos denovo?')
	if pergunta == 'i':
		if soma % 2 != 0:
			print(f'Parabéns! Eu escolhi {maquina} e voce venceu! vamos denovo?')
			vezes_ganha += 1
		if soma % 2 == 0:
			print(f'Eu venci! Escolhi {maquina} e ganhei! Vamos denovo?')
	cont += 1
	pergunta2 = str(input('Voce quer ir denovo? [S/N]')).lower()						
	if pergunta2 == 'n':
		break
print(f'Ok então! nos jogamos {cont} vezes e voce venceu {vezes_ganha}.')		