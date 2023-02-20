time = []
dados = {}
gols = []
saida = False
while not saida:
    dados = {}
    dados['nome'] = input('Nome do Jogador: ')
    jogos = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for c in range(1, jogos + 1):
        pergunta = int(input(f'Gols na partida {c}: '))
        gols.append(pergunta)
    dados["gols"] = gols[:]
    dados["total"] = sum(dados['gols'])
    gols.clear()  
    time.append(dados.copy())
    pergunta2 = str(input('Quer continuar? [S/N] ')).upper()
    if pergunta2 == 'N':
        break
    if pergunta2 != 'S' and pergunta != 'N':
        while not saida:
            pergunta2 = str(input('ERRO! Apenas [S/N]\nQuer continuar? [S/N]')).upper()
            if pergunta2 == 'S':
                break
            elif pergunta2 == 'N':
                saida = True   
print('='*50)                                      
print('cod    ', end = ' ')
for c in time[0].keys():
    print(f'{c: <15}', end = ' ')
print()    
print('='*50)  
for c, v in enumerate(time):
    print(f'{c: <5}', end = ' ')
    for g in v.values():
        print(f'{str(g): <17}', end = ' ')
print('-'* 50) 
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        print('<= VOLTE SEMPRE =>')
        break
    elif busca >= len(time):
        print(f'ERRO! Não existe jogador com o id {busca}') 
    else:
        print('=='* 30)
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for g, v in enumerate(time[busca]['gols']):
            print(f'    No jogo {g + 1} fez {v} gols')