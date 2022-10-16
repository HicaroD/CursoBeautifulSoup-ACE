import requests
from bs4 import BeautifulSoup

"""
Criando um objeto BeatifulSoup
"""

html_doc = requests.get("https://www.populationpyramid.net/pt/popula%C3%A7%C3%A3o/2022/")
soup = BeautifulSoup(html_doc.text, "html.parser")
print(soup.prettify)

"""
Acessando tags HTML
"""
print(soup.title)

print(soup.title.name)

print(soup.title.string)

print(soup.title.parent.name)

print(soup.p)

print(soup.a)

print(soup.find_all('a'))

print(soup.find(id = 'menu'))

"""
Acessando os atributos das tags
"""
for link in soup.find_all('a'):
  print(link.get('href'))
  print('-=-=-=-=-=-=-=-=-=-=-')

"""
Extraindo texto do conteúdo
"""
print(soup.get_text())
