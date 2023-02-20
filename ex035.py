a = float(input('Qual o valor da primeira reta? '))
b = float(input('Qual o valor da segunda reta? '))
c = float(input('Qual o valor da terceita reta? '))
if a + b > c and c + a > b and c + b > a:
    print('Pode formar um triangulo')
else:
    print('não pode formar um triangulo')