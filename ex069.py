cont = 0
maior18 = 0
homens = 0
menor20 = 0
while True:	
	Idade = int(input('Qual a idade da pessoa? '))
	sexo = str(input('qual o sexo da pessoa? [M/F]')).lower()
	if Idade > 18:
		maior18 += 1
	if sexo == 'm':
		homens += 1
	if sexo == 'f' and Idade < 20:
		menor20 += 1
	cont += 1	
	pergunta2 = str(input('Quer continuar? [S/N]')).lower()
	if pergunta2 == 'n':
		break
print(f'Pessoas cadastradas: {cont}')
print(f'Maiores de 18: {maior18}')
print(f'Homens: {homens}')
print(f'Mulheres com menos de 20 anos: {menor20}')											