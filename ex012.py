pre = float(input('Qual o preço do produto?\n R$'))
c = pre * 5 / 100
r = pre - c
print('o produto que custava R${}, com o desconto de 5% ira ficar com o valor de R ${:.2f}'.format(pre, r))

