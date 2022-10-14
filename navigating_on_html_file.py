from bs4 import BeautifulSoup
import requests


def main():
    response = requests.get(
        "https://www.populationpyramid.net/pt/popula%C3%A7%C3%A3o/2022/"
    )

    if response.status_code != 200:
        print("Não foi possível obter a página HTML")

    """
    Esse comando irá criar um objeto da classe BeautifulSoup (isso será explicado em
    mais detalhes por outros integrantes)
    """
    html_doc = response.text
    soup = BeautifulSoup(html_doc, "html.parser")

    """
    Esse comando abaixo irá buscar a primeira tag <a> dentro do HTML
    """
    print(soup.a)

    """
    Esse comando abaixo irá extrair o texto de dentro da primeira tag <a> dentro do HTML
    """
    print(soup.a.text)

    """
    Esse comando irá extrair todas as children da primeira tag <div> que aparecer dentro
    do HTML.
    """
    for child in soup.div.children:
        print(child)

    """
    Esse comando irá extrair todos os parent da primeira tag <div> que aparecer dentro
    do HTML.
    """
    for parent in soup.div.parents:
        print(parent.name)

if __name__ == "__main__":
    main()
