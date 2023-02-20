#valor x 110 / 100 - valor
preco = float(input('Quanto foi o produto? '))
pergunta = int(input('Qual Vai ser a forma de pagamento? digite 0 para a vista e 1 para parcelado: '))
if pergunta == 0:
	vista = int(input('Credito ou dinheiro? Digite 0 para credito ou 1 para dinheiro: '))
	if vista == 0:
		credito_vista = preco * 95 / 100
		print('O seu produto ficou por R${}'.format(credito_vista))
	else:
		dinheiro_vista = preco * 90 / 100
		print('O seu produto ficou por R${}'.format(dinheiro_vista))
else:
	parcelado = int(input('Vai parcelar em quantas vezes? '))
	if parcelado == 2:
		mes = preco / 2
		print('O Valor do produto vai ser de {} por mes!'.format(mes))			
	else:
		parcelado2 = preco * 120 / 100
		aomes = parcelado2 / parcelado
		print('Voce vai pagar {:.2f} por mes com juros de 20%.'.format(aomes))										