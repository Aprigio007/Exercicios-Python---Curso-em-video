import time
numeros = ('um', 'dois', 'Tres', 'quatro', 'cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 
'Dezenove', 'vinte')
while True:
	pergunta = int(input('Qual numero voce deseja ver? entre 1 e 20 '))
	if pergunta >= 21 or pergunta <= 0:
		while pergunta <= 0 or pergunta >= 21:
			pergunta = int(input('Resposta inválida, tente novamente. Um numero entre 1 e 20: '))
	print(f'O número digitado é {numeros[pergunta - 1]}.')
	pergunta2 = str(input('Quer ir denovo? [S/N]: ')).lower()
	if pergunta2 == 'n':
		print('Fim do programa. Obrigado por usar! ')
		time.sleep(2)
		break	