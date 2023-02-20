pergunta = 0
soma = 0
total = 0
while pergunta != 999:
	pergunta = float(input('Digite um valor aleatorio. [999 para parar]'))
	soma = soma + pergunta
	total += 1
print('A quantidade de vezes perguntada é {} e a soma dos valores perguntados é {}.'.format(total - 1, soma - 999))	