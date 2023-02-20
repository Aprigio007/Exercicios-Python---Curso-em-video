#lendo os números
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('digite o terceiro número: '))
#n1 ganhando em maior
if n1 > n2 and n1>n3:
    maior = n1
#n2 ganhando em maior
if n2 > n1 and n2 > n3:
    maior = n2
#n3 ganhando em maior    
if n3 > n1 and n3 > n2:
    maior = n3
#n1 ganhando em menor
if n1 < n2 and n3 > n1:
    menor = n1
# n2 ganhando em menor
if n2 < n3 and n2 < n1:
    menor = n2
#n3 ganhando em menor
if n3 < n1 and n3 < n2:
    menor = n3
print('O maior número é {}.'.format(maior))
print('O menor número é {}.'.format(menor))

