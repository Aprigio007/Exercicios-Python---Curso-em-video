list = []
pos = 0
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > list[-1]:
        list.append(num)
        print('Valor adicionado ao final da lista...')    
    else:
        while pos < len(list):            
            if num <= list[pos]:
                list.insert(pos, num)
                print(f'Valor adicionado com sucesso na posição {pos}...')
                break
            pos += 1              
print(f'Os valores digitados foram: {list}')
