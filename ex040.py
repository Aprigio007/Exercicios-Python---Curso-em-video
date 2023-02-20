n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunta nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
media = (n1 + n2 + n3 + n4) /4
if media >=7 and media <= 10:
	print('Aprovado')
elif media <=5 and media >= 0:
	print('Reprovado')	
else:
	print('Recuperação')	