numero = input('digite um numero de 1 a 9999: ')

#separação dos números 
separar = numero[:]

#unidade
unidade = (separar[3])
print('unidade: {}'.format(unidade))

#dezena
dezena = (separar[2])
print('dezena: {}'.format(dezena))

#centena
centena = (separar[1])
print('centena: {}'.format(centena))

#milhar
milhar = (separar[0])
print('milhar: {}'.format(milhar))