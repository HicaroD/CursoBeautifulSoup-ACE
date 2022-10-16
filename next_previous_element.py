import requests
from bs4 import BeautifulSoup
url='https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

find_a = soup.find_all("a")[4]
print('-------------------------------------------------------------------------')
print(find_a)
print('-------------------------------------------------------------------------')
#next.element tras o proximo elemento.
print(find_a.next_element)
print('-------------------------------------------------------------------------')
#previous_element tras o elemento anterior
print(find_a.previous_element)




