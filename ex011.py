lar = float(input('qual a largura da parede?'))
alt = float(input('qual a altura da parede?'))
area = lar * alt
r = area / 2
print('sua parede tem dimensões {:.0f}x{:.0f} e tem área {:.0f}. Vai ser necessário {}L de tinta para pintar completamente. '.format(lar, alt, area, r))