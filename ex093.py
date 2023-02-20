def linha():
	print('-=' * 30)
dicionario = {}
lista = []
soma = 0
nome = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {nome} jogou? '))
dicionario['Nome'] = nome
for c in range(1, partidas + 1):
	lista.append(int(input(f'Quantos gols na partida {c}? ')))
soma = sum(lista)
dicionario['gols'] = lista[:]
dicionario['total'] = soma
linha()
print(dicionario)
linha()
for k, i in dicionario.items():
	print(f'O campo {k} tem o valor {i}.')
linha()
print(f'O jogador {nome} jogou {partidas} partidas.')
for k, i in enumerate(lista):
	print(f'     Na partida {k + 1}, fez {i} gols.')
print(f'Foi um total de {soma} gols.')				