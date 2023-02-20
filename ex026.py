nome = str(input('Digite uma frase:)).upper().replace(' ','')

#quantas letras A tem no texto 
print('Sua frase tem {} Letras A.'.format(nome.count('A')))

#quando aparece a primeira letra A
print('A primeira letra A aparece em {}.'.format(nome.find('A')+1))

#quando aparece a ultima letrq A
print('A ultima letra A aparece em {}.'.format(nome.rfind('A')+1))