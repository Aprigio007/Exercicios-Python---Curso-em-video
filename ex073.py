times = ('America mineiro', 'Athletico paranaense', 'Atletico mineiro', 'Bahia', 'Botafogo', 'Corinthias', 'Coritiba', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Gremio', 'Internacional', 'Palmeiras', 'Bragantino', 'Santos', 'São paulo', 'Vasco da gama')
primeiros_5 = times[:5]
ultimos_4 = times[16:]
ordem_alfabetica = sorted(times)
sao_paulo = times.index('São paulo') + 1
print('Os primeiros 5 times do Brasileirão é {}\n'.format(primeiros_5))
print('Os ultimos 4 são {}\n'.format(ultimos_4))
print('Os times em ordem alfabética são {}\n'.format(ordem_alfabetica))
print('O são paulo está na {} posicão.'.format(sao_paulo))