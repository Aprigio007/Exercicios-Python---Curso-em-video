nome = input('digite seu nome completo: ')

#Todas em letras maiusculas 
nome_maiusculo = nome.upper()
print('o nome em letras maiusculas fica {}.'.format(nome_maiusculo))

#Em minúsculas
nome_minusculo = nome.lower()
print('o nome em minúsculas fica {}.'.format(nome_minusculo))

#contar caracteres
sem_espaco = nome.replace(" ", '')
contar_letras = len(sem_espaco)
print('a quantidade de letras é: {}.'.format(contar_letras))

#numero de caracteres do primeiro nome
dividir = nome.split(' ')
primeiro_nome = dividir[0]
contar = len(primeiro_nome)
print('a quantidade de letras do primeiro nome é: {}.'.format(contar))