maior = 0
menor = 0
for c in range(1, 8):
	pergunta = int(input('qual data a {} pessoa nasceu?'.format(c)))
	nasceu = 2023 - pergunta
	if nasceu < 18:
		menor = menor + 1
	else:
		maior = maior + 1	
print('Existem {} pessoas maiores de idade e {} menores de idade.'.format(maior, menor))						