lista = [ [ ], [ ], ]
numero = []
for c in range(0, 7):
	numero.append(int(input(f'Digite o {c + 1} valor: ')))
	if numero[0] % 2 == 0:
		lista[0].extend(numero)
	elif numero[0] % 2 != 0:
		lista[1].extend(numero)
	numero.clear()
lista[1].sort()
lista[0].sort()
print(f'O total de números pares foram {lista[0]}')
print(f'E o total de números ímpares foram {lista[1]}')				