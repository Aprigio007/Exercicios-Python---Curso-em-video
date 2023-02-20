import moeda
n = int(input('Digite um número: '))
print(f'O Dobro do valor é {moeda.dobro(n)}\nO Valor -10% é {moeda.diminuir(n)}\nO Valor +10% é {moeda.aumentar(n)}\nA metade do valor é {moeda.metade(n)} ')