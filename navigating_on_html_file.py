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
    print(soup.a)
    print(soup.div.div.p.text == "Silva")

if __name__ == '__main__':
    main()