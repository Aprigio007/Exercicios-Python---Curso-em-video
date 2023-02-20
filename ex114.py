import requests
try:
	site = requests.get('https://youtube.com.br')
except:
	print('\033[31mNão consegui acessar o site do youtube ):\033[m')	
else:
	print('\033[32mConsegui acessar o site do youtube!\033[m')	