import math
angulo = float(input('digite um angulo: '))
cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('o seno é {:.2f}'.format(seno))
print('o cosseno é {:.2f}'.format(cosseno))
print('e a tangente é {:.2f}'.format(tangente))
