pessoas = list()
recebimento = []
while True:
	recebimento.append(str(input('Nome: ')))
	recebimento.append(float(input('Nota 1: ')))
	recebimento.append(float(input('Nota 2: ')))
	pessoas.append(recebimento[:])
	recebimento.clear()
	pergunta = str(input('Quer continuar? [S/N] ')).lower()
	if pergunta == 'n':
		break
print('=' * 40)		
print('No.',' ' * 2, 'Nome', ' ' *15, 'MÉDIA')
print('=' * 30)
for c in range(0, len(pessoas)):
	print('{:<4} {:<23} {:<6}'.format(c, pessoas[c][0], (pessoas[c][1] + pessoas[c][2]) / 2))
while True:
	opc = int(input('Digite a posição para ver as notas do aluno: [999 para interromper] '))
	if opc > len(pessoas) and opc != 999:
		print('Número não encontrado no sistema, tente novamente!')
	print('-='*30)
	if opc == 999:
		print('Encerrando sistema...')
		break
	if opc <= len(pessoas):
		print(f'As notas do {pessoas[opc][0]} são: {pessoas[opc][1]} e {pessoas[opc][2]}')
			
