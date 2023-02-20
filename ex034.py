salario = int(input('Qual o salario do funcionario? R$'))
if salario > 1250:
    salario2 = salario * 10 / 100
    salario3 = salario2 + salario 
else:
    salario2 = salario * 15 / 100
    salario3 = salario2 + salario 
print('Com um salario de R${:.2f}, o funcionario ira obter um salario de R${:.2f}.'.format(salario, salario3))    