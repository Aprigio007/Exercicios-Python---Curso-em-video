print('LISTA DE PREÇOS')
tupla = ('Caderno', 10.00, 'lápis', 2.00, 'mochila', 20.00, 'estojo', 5.00, 'Celular', 1200, 'Computador', 3000)
for items in range(0, len(tupla)):
  if items % 2 != 0:
    print('.' * 30, 'R$', tupla[items])
  elif items % 2 == 0:
    print(tupla[items], end = ' ')