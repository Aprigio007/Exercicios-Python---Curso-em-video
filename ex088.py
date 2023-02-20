import random
import time
print('='* 30)
print('JOGOS DA MEGASENA')
print('=' * 30)
lista = []
jogos = []
pergunta = int(input('Quantos jogos voce quer que eu sorteie?'))
for c in range(0, pergunta + 1):
	lista.append(jogos[:])
	jogos.clear()
	for l in range(0, 6):
		jogos.append(random.randint(1, 60))
for c in range(1, len(lista)):
	time.sleep(1)
	print(f'Jogo {c}: {lista[c]}')	
print('-=' * 10,'>', 'BOA SORTE!', '<', '-=' *10)						