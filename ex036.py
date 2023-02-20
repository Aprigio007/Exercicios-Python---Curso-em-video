casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual é o seu salario? '))
anos = int(input('Em quantos anos voce vai pagar a casa? '))
anomes = anos * 12
valor = casa / anomes
porcentagem = valor * 30 / 100
if casa >= porcentagem:
	print('Negado')
else:
	print('Aceito')	
