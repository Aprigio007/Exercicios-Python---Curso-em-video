list = []
mai = 0
men = 0
for c in range(0, 5):
	num = int(input(f'Fale um valor para a posição {c}: '))
	list.append(num)
	if c == 0:
		mai = num
		men = num
	if c != 0:
		if num > mai:
			mai = num
		if num < men:
			men = num							    				
print(f'Os valores digitatos foram: {list}')
print(f'O menor foi {men} nas posições:', end = ' ')
for po, nu in enumerate(list):
	if nu == men:
		print(f'{po}...', end = ' ' )
print(f'\nO maior foi {mai} nas posições:', end = ' ')
for p, n in enumerate(list):
	if n == mai:
		print(f'{p}...' , end = ' ')