# iniciar variaveis
dicionario = {}
contador = 0
#importar a biblioteca random
from random import randint
from time import sleep
from operator import itemgetter
#sortear 4 valores e guardar em um dicionario com os respectivos nomes
print('Valores sorteados:')
for c in range(1, 5):
	dicionario[f'jogador{c}'] = randint(1, 6)
	print(f'Jogador{c} tirou: {dicionario[f"jogador{c}"]}')
	sleep(1)
#organizar o dicionario
ranking = dict(sorted(dicionario.items(), key= itemgetter(1), reverse = True))
#imprimir os resultados
print('-=' * 10, 'RANKING', '-=' * 10)
for k, v in (ranking.items()):
	contador += 1
	print(f'   {contador}ª lugar: {k} com {ranking[k]}')