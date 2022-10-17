from bs4 import BeautifulSoup
import requests


def main():
    headers = {"User-Agent": "Mozilla/5.0"}

    website = "https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)"
    response = requests.get(
        website,
        headers=headers,
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
    Esse comando abaixo irá buscar a primeira tag <div> dentro do HTML
    """
    print(soup.div)

    """
    Esse comando abaixo irá extrair o texto de dentro da primeira tag <p> dentro do HTML
    """
    print(soup.p.text)

    """
    Esse comando irá extrair todas as children da primeira tag <div> que aparecer dentro
    do HTML.
    """
    for child in soup.p.children:
        print(child)

    """
    Esse comando irá extrair todos os parent da primeira tag <div> que aparecer dentro
    do HTML.
    """
    print(soup.b)
    for parent in soup.b.parents:
        print(parent.name)

if __name__ == "__main__":
    main()
