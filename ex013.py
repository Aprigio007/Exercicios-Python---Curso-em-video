sa = float(input('Quanto o funcionário ganha?:\nR$'))
r = (sa * 15 / 100) + sa
print('O funcionário que recebia R${}, com o aumento de 15% irá passar a receber R${}.'.format(sa, r))