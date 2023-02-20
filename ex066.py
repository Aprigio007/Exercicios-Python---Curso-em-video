soma = 0
contagem = 0
while True:
	pergunta = int(input('Digite um número. [999 para parar] '))
	if pergunta == 999:
		break
	soma += pergunta
	contagem += 1
print(f'Números lidos: {contagem}')
print(f'Soma dos números: {soma}')	
		