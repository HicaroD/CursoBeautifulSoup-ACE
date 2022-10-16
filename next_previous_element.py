import requests
from bs4 import BeautifulSoup
url='https://www.populationpyramid.net/pt/popula%C3%A7%C3%A3o/2022/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

find_a = soup.find_all("a")[0]
print('-------------------------------------------------------------------------')
print(find_a)
print('-------------------------------------------------------------------------')
#next.element tras o proximo elemento.
print(find_a.next_element)
print('-------------------------------------------------------------------------')
#previous_element tras o elemento anterior
print(find_a.previous_element)
print('-------------------------------------------------------------------------')




