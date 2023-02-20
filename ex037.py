numero = int(input('Digite um número aleatorio: '))
escolha = int(input('Digite a opcão desejada para conversão, use -1 para binário, -2 para octal e -3 para hexadecimal: '))
if escolha == -1:
    numero_convertido = bin(numero) 
    print('O número convertido em binário é {}'.format(numero_convertido))
elif escolha == -2:
    numero_convertido = oct(numero)
    print('O seu número convertido em octal fica {}.'.format(numero_convertido))
elif escolha == -3:
    numero_convertido = hex(numero)
    print('Seu numero convertido em hexadecimal fica {}'.format(numero_convertido))
else:
    print('Opcão invalida, execute o programa e tente novamente!')