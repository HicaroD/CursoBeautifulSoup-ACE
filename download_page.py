from bs4 import BeautifulSoup
import requests

def main():
    response = requests.get("https://www.populationpyramid.net/pt/popula%C3%A7%C3%A3o/2022/", headers = {"User-Agent": "Mozilla/5.0"})

    if response.status_code != 200:
        print("Não foi possível obter a página")
        exit(1)

    print(response.text)

if __name__ == "__main__":
    main()
