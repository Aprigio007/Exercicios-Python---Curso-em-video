
def aumentar(a, f = False):
	r = a * 110 / 100
	if f == True:
		return '{:.2f}'.format(r)
	else:
		return r	
def diminuir(a, f = False):
	t = a * 10 / 100
	r = a - t
	if f == True:
		return '{:.2f}'.format(r)
	else:
		return r
def dobro(a, f = False):
	r = a * 2
	if f == True:
		return '{:.2f}'.format(r)
	else:
		return r	
def metade(a, f = False):
	r = a / 2
	if f == True:
		return '{:.2f}'.format(r)
	else:
		return r
def resumo(d = 0,a = 10,de =10):
	dobro = d * 2
	metade = d / 2
	aumento = d * (100 + a) / 100
	deducao = d - (d * de / 100)
	print('-' * 30)
	print(f'{"RESUMO DO VALOR": >21}')
	print('-' * 30)
	print(f'Preço Analisado:     R${d:.2f}')
	print(f'Dobro:               R${dobro:.2f}')
	print(f'Metade:              R${metade:.2f}')
	print(f'Aumento de {a}%:      R${aumento:.2f}')
	print(f'Dedução de {de}%:      R${deducao:.2f}')											