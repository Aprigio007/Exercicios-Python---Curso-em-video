def leiadinheiro(msg):
	while True:
		n = str(input(msg)).replace(',', '.').strip()
		if n.isdigit():
			return int(n)
			break
		elif '.' in n:
			return float(n)
			break	
		else:
			print(f'\033[31mERRO: "{n}" é um preço inválido!\033[m')		