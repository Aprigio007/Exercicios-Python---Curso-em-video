print('Gerador de Pa')
print('=' * 15)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
num_termo = 10
i = 1
pergunta2 = False
while not pergunta2:
	print(termo, end = ' --> ')
	termo = termo + razao
	i = i + 1
	if i >= 11:
		i = 1
		pergunta = int(input('Quer continuar? \n [0] Sair \n [1] Fazer mais 10 \n'))
		if pergunta == 0:
			pergunta2 = True