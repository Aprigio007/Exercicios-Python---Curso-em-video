altura = float(input('Digite a sua altura em CM: '))
peso = float(input('Digite seu peso em KG: '))
imc = peso / altura ** 2
if imc <= 18.5:
	print('Voce está abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
	print('Voce está no peso ideal. Parabéns!')
elif imc >= 25.1 and imc <= 30:
	print('Voce esta em sobrepeso!')
elif imc >= 30 and imc <= 40:
	print('Voce esta obeso!')
elif imc > 40.1:
	print('Voce está em obesidade mórbida')
else:
	print('Valor inválido. Tente novamente!')				