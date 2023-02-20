import math
n = int(input('Digite o numero para calcular o fatorial: '))
f = math.factorial(n)
print(f'{n}! =' , end = ' ')
for c in range(n, 0, -1):
	if c == 1:		
		print(f'{c} =', end = ' ')
	else:
		print(f'{c} x', end = ' ')
print(f)			