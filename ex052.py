print('====================')
print('VERIFICADOR DE NUMEROS PRIMOS')
print('====================')
numero = int(input('Digite um número inteiro: '))
for c in range(numero - 1, 1, -1):
	if numero % c == 0:
		primo = 'Não é um número primo'
	elif numero % c > 0:
		primo = 'É um numero primo'		
print(primo)					