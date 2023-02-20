import datetime
ano = int(input('Digite o ano que quer calcular, se for o ano atual digite 0:'))
calculo = ano % 4
if ano == 0:
    anoatual = datetime.datetime.now().year
    anoatual2 = anoatual % 4
    if anoatual2 == 0:
        print('O ano de {} é bisexto'.format(anoatual))
    else:
        print('O ano de {} não é bisexto.'.format(anoatual))
else:
    if calculo == 0:
        print('O ano {} é bisexto.'.format(ano))
    else:
        print('O ano {} não é bisexto.'.format(ano))
    
