soma = 0
for c in range(1, 7):
	num = int(input('Digite um número inteiro: '))
	if num % 2 == 0:
		soma = soma + num
print('O valor dos resultados pares somados é {}'.format(soma))		