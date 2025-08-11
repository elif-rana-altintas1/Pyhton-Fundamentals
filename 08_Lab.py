

from requests import get
from pprint import pprint

api_endpoint = 'https://newsapi.org/v2/everything?q=tesla&from=2025-04-24&sortBy=publishedAt&apiKey=47f3419f49864ca889f632677d485de1'

response = get(api_endpoint)

data = response.json()

# pprint(data['articles'][1])

# pprint(f"Author: {data['articles'][1]['author']}")
# pprint(f"Description: {data['articles'][1]['description']}")
# pprint(f"Publish Date: {data['articles'][1]['publishedAt']}")



#* kullanıcıdan yazar ismi alalım ve bu yazarın makelesini ekrana yazdıralım
author_name = input('Author Name: ')

for article in data['articles']:
    if article.get('author') == author_name:
        print(article)