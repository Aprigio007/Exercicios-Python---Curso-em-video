frase = str(input(' Digite uma frase: ')).replace(' ', '').upper()
inversao = frase[:: -1]
if inversao == frase:
	print('Temos um palíndromo! ')
else:
	print('A frase não é um palíndromo!')	