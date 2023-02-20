
expressao = str(input('Digite uma expressão: '))
if expressao.count(')') == expressao.count('('):
	print('A expressão é válida!')
else:
	print('A expressão é inválida!')												