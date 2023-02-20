a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))
if a + b > c and c + a > b and b + c > a:
	if a == b == c:
		print('Seu triangulo é equilátero')
	elif a == b or c == a or c == b:
		print('seu triangulo é isósceles')
	else:
		print('Seu triangulo é escaleno')
else:
	print('As medidas fornecidas não formam um triangulo')				