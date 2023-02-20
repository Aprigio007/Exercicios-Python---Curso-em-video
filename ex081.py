def organizar():
	print('=' * 30)
lista = []
while True:
	pergunta = int(input('Digite um número: '))
	organizar()
	lista.append(pergunta)
	pergunta2 = str(input('Quer continuar? [S/N]: '))
	organizar()
	if pergunta2 == 'n':
		break
lista.sort(reverse = True)
print('\n' * 100)		
print(f'Foram digitados {len(lista)} números')
organizar()	
print(f'A lista ordenada fica {lista}')
organizar()
if 5 in lista:
	print('O valor 5 está na lista!')
else:
	print('O valor 5 não está na lista!')		