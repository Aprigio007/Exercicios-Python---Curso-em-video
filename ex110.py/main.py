from utilidadesCeV import moeda
import os
os.system('clear')
v = int(input('Qual valor quer analisar? '))
a = int(input('Qual o aumento? '))
d = int(input('Qual a dedução? '))
moeda.resumo(v, a, d)