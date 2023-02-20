from time import sleep
while True:
	print(f'\033[30;43m{"=": <2}' * 30)
	print(f'{"Sistema de Ajuda Python": <60}')
	print(' =' * 30)
	print('\033[m', end = ' ')
	print()
	ajuda = input('Função da biblioteca -> ')
	if ajuda == 'fim':
		print('Encerrando...')
		sleep(1)
		break
	print(f'\033[30;44m{"="}' * 60)
	print(f"Acessando manual de comando '{ajuda}", ' ' * 29)
	sleep(1.5)
	print(f'{"="}' * 60)
	print('\033[m')
	print('\033[30;47m')
	help(ajuda)