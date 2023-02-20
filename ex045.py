#0 = pedra
#1 = papel
#2 = tesoura
import random
jogo = [0,1,2]
escolha = random.choice(jogo)
humano = int(input('Tente vencer de mim no jokenpo! Escolha 0 para pedra, 1 para papel e 2 tesoura. '))
if escolha == 0:
	if humano == 0:
		print('Tambem escolhi pedra. Empatou!')
	elif humano == 1:
		print('escolhi pedra, Perdi.') 
	else:
		print('Escolhi pedra, Ganhei')
elif escolha == 1:
	if humano == 0:
		print('Escolhi Papel, Ganhei!')
	elif humano == 1:
		print('Também escolhi papel, Empatamos!')
	else:
		print('escolhi papel, perdi!')
elif escolha == 2:
	if humano == 0:
		print('Escolhi Tesoura, Perdi')
	elif humabo == 1:
		print('Escolhi Tesoura, Venci!')	
	else:
		print('Também escolhi Tesoura, Empatamos!')
elif humano >= 3:
	print('Opção inválida. Tente novamente!')														