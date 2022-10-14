import requests
from bs4 import BeautifulSoup

html_doc = requests.get("https://www.terra.com.br/esportes/futebol/brasileiro-serie-a/tabela/")

sopa = BeautifulSoup(html_doc.text, 'html.parser')

nomes_times = sopa.find_all('td', {'class': 'main team-name'})
pontos_times = sopa.find_all('td', {'class': 'points'})
vitorias_times = sopa.find_all('td', {'title': 'Vitórias'})
derrotas_times = sopa.find_all('td', {'title': 'Derrotas'})
empates_times = sopa.find_all('td', {'title': 'Empates'})

for i, _ in enumerate(nomes_times):
  time_nome = nomes_times[i].text.replace('>>', '')
  qntd_pontos = pontos_times[i].text
  qntd_vitorias = vitorias_times[i].text
  qntd_derrotas = derrotas_times[i].text
  qntd_empates = empates_times[i].text

  print(f'Time: {time_nome}', end='')
  print(f'Quantidade de Pontos: {qntd_pontos}')
  print(f'Quantidade de Vitórias: {qntd_vitorias}')
  print(f'Quantidade de Derrotas: {qntd_derrotas}')
  print(f'Quantidade de Empates: {qntd_empates}')
  print('-=-=-=-=-=-=-=-=-=-=-=-=-')
