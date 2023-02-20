soma = 0
maior1000 = 0
nomebarato = ' '
menor = 0
contagem = 0
print('-'*20)
print('LOJA AZ TRICKS')
print('-'*20)
while True:
	Nome = str(input('Qual é o nome do produto? '))
	preco = float(input('Qual o preco do produto? '))
	contagem += 1
	soma = soma + preco
	if preco > 1000:
		maior1000 += 1
	if contagem == 1:
		nomebarato = Nome
		menor = preco
	elif contagem != 1 and preco < menor:
		nomebarato = Nome
	pergunta2 = str(input('Quer continuar? [S/N] ')).lower()
	if pergunta2 == 'n':
		break
print(f'O valor total da compra foi: {soma}')
print(f'{maior1000} produtos ultrapassam R$1000')
print(f'O produto mais barato foi {nomebarato}')			