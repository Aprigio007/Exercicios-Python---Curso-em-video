matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
coluna_3 = 0
for l in range(0, 3):
	for c in range(0, 3):
		matriz[l][c] = int(input(f'Digite o valor da posição {l} {c}: '))
		if c == 2:
			coluna_3 = coluna_3 + matriz[l][2]
		if matriz[l][c] % 2 == 0:
			pares = pares + matriz[l][c]
for l in range(0, 3):
	for c in range(0, 3):
		print(f'[ {matriz[l][c]} ]', end = ' ')
	print()
print(f'A soma dos números pares são {pares}')
print(f'A soma da coluna 3 é {coluna_3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')		