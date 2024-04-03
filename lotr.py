import requests


lista_livros = ['The Fellowship Of The Ring', 'The Two Towers', 'The Return Of The King' ]

dados_livros = []

headers = {
    "Authorization" : "Bearer ht4b6M6jOYJO5hIEIxQB" 
}

for livros in lista_livros:
    url = 'https://the-one-api.dev/v2/book' .format(livros)
    req = requests.get(url)
    book = req.json()

    print(book)
    