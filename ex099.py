from time import sleep
def maior(*num):
	print('Analisando os valores passados...')
	for c in num:
		print(c, end = ' ', flush = True)
		sleep(0.5)
	print(f'Foram digitados {len(num)} valores ao todo.')
	print(f'O maior valor informado foi {max(num)}')
	print('-' * 30)
maior(7,8,10)
maior(7,10,8,2,8)
maior(2,4,8,2)
maior(2,5,100,13)			