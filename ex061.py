print('====================')
print('10 TERMOS DE UMA PA')
print('====================')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
num_termo = 10
i = 1
while i <= 10:
	print(primeiro , end = ' --> ')
	primeiro += razao
	i = i + 1
print('Acabou')