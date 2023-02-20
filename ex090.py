situacao = {}
nome = input('Nome: ')
media = float(input(f'A média do(a) {nome}: '))
situacao['nome'] = nome
situacao['media'] = media
if media < 6:
	situacao['Situação'] = 'Reprovado'
elif media >= 6 and media < 7:
	situacao['Situação'] = 'Recuperação'
elif media >= 7:
	situacao['Situação'] = 'Aprovado'
print('=-' * 30)
for c, v in situacao.items():
	print(f'   - {c} é igual a {v}')			