import requests
from bs4 import BeautifulSoup
url='https://www.terra.com.br/esportes/futebol/brasileiro-serie-a/tabela/'

response = requests.get(url)

sopao = BeautifulSoup(response.text, 'html.parser')

teste = sopao.find("tr", {'data-idteam':'1180'})

nome_time=teste.contents[2].text.replace('>>',"")
pontos_time=teste.contents[4].text.replace('>>',"")
vitorias_time=teste.contents[5].text.replace('>>',"")
empates_time=teste.contents[6].text.replace('>>',"")
derrotas_time=teste.contents[7].text.replace('>>',"")

print('-------------------------------------------------------------')
print(f'O meu time e o {nome_time}')
print(f'Pontos: {pontos_time}')
print(f'Vitorias {vitorias_time} ')
print(f'Empates: {empates_time} ')
print(f'Derrotas: {derrotas_time} ')


