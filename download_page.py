import requests


def main():
    """
    Esse código serve para obter a página que será usada no minicurso.

    Por quê o headers? Porque alguns websites identificam que nós estamos tentando
    acessar o site de forma automática usando algum script, isso, muitas vezes,
    geram problemas e o website não libera o acesso. Para resolver isso, usamos
    o headers com User-Agent da Mozilla para simular um usuário real acessando o
    website.
    """
    response = requests.get(
        "https://www.populationpyramid.net/pt/popula%C3%A7%C3%A3o/2022/",
        headers={"User-Agent": "Mozilla/5.0"},
    )

    """
    Quando fazemos uma requisição, a resposta pode ser boa ou ruim. Isso porque podemos
    ter problema de Internet, problemas no servidor e etc. No caso de sucesso, o 
    código de status (status_code) deve ser igual a 200. Caso contrário, deu errado, sendo
    assim não podemos prosseguir com o código.
    """
    if response.status_code != 200:
        print("Não foi possível obter a página")
        exit(1)

    """
    No caso de sucesso na requisição, printamos a página HTML obtida
    """
    print(response.text)


if __name__ == "__main__":
    main()
