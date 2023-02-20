#ler a distancia percorrida
#calcular o valor que tem que pagar 
#e se passar de 200km tem desconto
distancia = int(input('diga a distancia percorrida em km: KM'))
calculo = distancia * 0.50
if distancia > 200:
    calculo2 = distancia * 0.45
    print('Parabéns! Voce ganhou um desconto, e sua viagem passou a custar R${:.2f}.'.format(calculo2))
else:
    print('Sua viagem custou R${:.2f}.'.format(calculo))
    