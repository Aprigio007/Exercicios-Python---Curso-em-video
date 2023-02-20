n1 = int(input('Digite o valor do primeiro numero: '))
n2 = int(input('digite o valor do segundo numero: '))
if n1 > n2:
    print('O primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
elif n1 == n2:
    print('Não existe valor maior, os dois sao iguais!')
else:
    print('Opcão invalida, execute o programa denovo e tente novamente!')