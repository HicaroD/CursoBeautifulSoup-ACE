from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

<div class="container">
    <p id="nome">Hícaro</p>
    <div class="inner-container">
        <p id="nome">Silva</p>
    </div>
</div>
"""

def main():
    soup = BeautifulSoup(html_doc, "html.parser")

    print(soup.a) # Primeira tag "a" encontrada no arquivo
    print(soup.div.div.p.text == "Silva") # Indo fundo nas tags do arquivo HTML

    for parent in soup.div.parents: # .parents retorna todos os parentes de uma tag
        if parent is not None:
            print(parent.name)

    print(soup.div.parent) # .parent retorna a tag mãe, aquela no qual a tag está contida

    for child in soup.div.children: # Navegando por todas as filhas
        print(child)

if __name__ == '__main__':
    main()