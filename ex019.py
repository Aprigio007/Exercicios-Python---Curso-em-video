import random
n1 = input('qual o nome do primeiro aluno? ')
n2 = input('qual o nome do segundo aluno?? ')
n3 = input('qual o nome do terceiro aluno ')
n4 = input('qual o nome do quarto aluno? ')
lista = [n1, n2, n3, n4]
sorteio = random.choice(lista)
print('o nome escolhido foi {}.'.format(sorteio))
