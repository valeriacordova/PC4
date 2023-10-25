import requests

url = 'https://unsplash.com/es/fotos/cachorro-de-golden-retriever-claro-en-campo-de-hierba-verde-durante-el-dia-atOlntWcO4k?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash'
response = requests.get(url)
with open('perro.jpg', 'wb') as f:
    f.write(response.content)
    pass