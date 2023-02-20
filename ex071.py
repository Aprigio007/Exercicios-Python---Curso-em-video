def colorir(texto, cor):
    cores = {'vermelho': '\033[31m',
             'verde': '\033[32m',
             'azul': '\033[34m',
             'amarelo': '\033[33m',
             'branco': '\033[37m',
             'preto': '\033[30m',
             'reset': '\033[0;0m'}
    return cores[cor] + texto + cores['reset']

print(colorir('='*20, 'verde'))
print(colorir('BANCO DO VASCO', 'vermelho'))
print(colorir('='*20, 'verde'))

valor = int(input(colorir('Qual valor deseja sacar? R$', 'branco')))

cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0

while valor >= 50:
    valor -= 50
    cont50 += 1
while valor >= 20:
    valor -= 20
    cont20 += 1
while valor >= 10:
    valor -= 10
    cont10 += 1
while valor >= 1:
    valor -= 1
    cont1 += 1

if cont50 != 0:
    print(colorir(f'O total de cédulas de 50 reais foi {cont50}', 'azul'))
if cont20 != 0:
    print(colorir(f'O total de cédulas de 20 reais foi {cont20}', 'azul'))
if cont10 != 0:
    print(colorir(f'O total de cédulas de 10 reais foi {cont10}', 'azul'))
if cont1 != 0:
    print(colorir(f'O total de notas de 1 real foi {cont1}', 'azul'))

print(colorir('~'*20, 'amarelo'))
