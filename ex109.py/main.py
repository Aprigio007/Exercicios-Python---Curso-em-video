import moeda
n = float(input('Digite um número: '))
print(f'O Dobro do valor é {moeda.dobro(n, f = True)}\nO Valor -10% é {moeda.diminuir(n, f = True)}\nO Valor +10% é {moeda.aumentar(n, f = True)}\nA metade do valor é {moeda.metade(n, f = True)} ')