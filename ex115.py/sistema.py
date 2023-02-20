import uteis
import os
from time import sleep
import arquivo
arq = 'pessoas.txt'
if not arquivo.verificararquivo(arq):
	arquivo.criararquivo(arq)	
while True:
	os.system('clear')
	uteis.cabecalho('MENU PRINCIPAL')
	sleep(0.5)
	uteis.menu(['Ver pessoas cadastradas','Cadastrar nova pessoa', 'Sair'])
	opc = uteis.leiaint('\033[33mSua opção: \033[m')
	if opc > 4:
		print('\033[31mERRO! Digite uma opção válida!\033[m')
		sleep(1.3)
	if opc == 1:
		os.system('clear')
		arquivo.lerarquivo(arq)
		print()
		p1 = str(input('[0] Voltar\n'))
	if opc == 2:
		os.system('clear')
		uteis.cabecalho('NOVO CADASTRO')
		nome = str(input('Nome: '))
		idade = uteis.leiaint('Idade: ')
		arquivo.cadastrar(arq, nome, idade)
		print()
		pergunta = input('Aperte enter para continuar\n')
	if opc == 3:
		os.system('clear')
		uteis.cabecalho('VOLTE SEMPRE')
		sleep(0.5)
		break