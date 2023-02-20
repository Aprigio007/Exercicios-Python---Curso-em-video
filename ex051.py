print('===============')
print('10 TERMOS DE UMA PA')
print('===============')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(1, 11):
	termo = primeiro + (c - 1) * razao
	print(termo)		