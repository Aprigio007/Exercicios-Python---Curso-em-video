#coletando a velocidade do carro
velocidade = int(input('Qual a velocidade do carro?'))
if velocidade > 80:
    diferenca = (velocidade - 80) * 7
if velocidade > 80:
    print('Você foi multado no valor de R${} por ultrapassar o limite de velocidade.'.format(diferenca))
else:
    print('Você está dirigindo dentro do limite de velocidade. Continue assim para garantir a segurança de todos na estrada.')