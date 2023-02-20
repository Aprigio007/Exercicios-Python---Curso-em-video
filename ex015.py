d = float(input('quantidade de dias que o carro foi utilizado: R$'))
k = float(input('quantidade de kilometros rodados pelo carro: R$'))
pd = d * 60
pk = k * 0.15
r = pd + pk
print('O valor total a se pagar é: R${:.2f}'.format(r))