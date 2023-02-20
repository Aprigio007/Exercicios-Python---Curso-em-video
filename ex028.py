import random
escolha = int(input('tente adivinhar que numero que eu escolhi de 0 a 5: '))
sorteio = random.randint(0,5)
if escolha == sorteio:
    print('PARABÉNS! VOCÊ GANHOU DE MIM!')
else:
    print('GANHEI! TENTE DENOVO GANHAR DE MIM!')