def ficha(jog = '<desconhecido>', gol = 0):
	print(f'O Jogador {jog} fez {gol} gols.')

n = str(input('Nome do jogador: '))
g = str(input('Gols: '))
if g.isnumeric():
	g = int(g)
else:
	g = 0
if n.strip() == '':
	ficha(gol = g)
else:
	ficha(n, g)		