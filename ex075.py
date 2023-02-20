números = int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o penúltimo numero: ')), int(input('Digite o último numero: '))
pares = []
for n in números:
  if n % 2 == 0:
    pares.append(n)
print(f'O número 9 apareceu {números.count(9)} vezes')
print(f'O número 3 apareceu na posição {números.index(3) + 1}')
if pares == []:
  print('Não existe números pares'  )
else:
  print(f'Os números pares são {pares}')