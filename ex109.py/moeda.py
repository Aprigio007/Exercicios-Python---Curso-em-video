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