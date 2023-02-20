pergunta = ' '
contagem = 0
maior = 0
menor = 0
soma = 0
while pergunta != 'n':
	numeros = float(input('-------------------- \n Digite um número: '))
	contagem += 1
	soma = soma + numeros
	if contagem == 1:
		maior = numeros
		menor = numeros
	elif contagem != 1:
		if numeros > maior:
			maior = numeros
		if numeros < menor:
			menor = numeros			
	pergunta = str(input('Quer continuar? [S/N] ')).lower()
	if pergunta != 's' and pergunta != 'n':	
		print('Resposta invalida, tente novamente')
		while pergunta != 's' and pergunta != 'n':
			pergunta = str(input('Quer continuar? [S/N]' ))
print('Voce digitou um total de {} numeros,o maior foi {} e o menor foi {}. A media deles foi {}.'.format(contagem, maior, menor, soma / contagem))	