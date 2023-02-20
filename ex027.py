nome = str(input('Digite seu nome completo: '))
primeiro_nome = nome.split()[0]
ultimo_nome = nome.split()[-1]

print('Prazer em conhecer!')
print('seu primeiro nome é {}'.format(primeiro_nome))
print('Seu ultimo nome é {}.'.format(ultimo_nome))
