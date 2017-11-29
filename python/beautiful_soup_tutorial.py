from bs4 import BeautifulSoup
import requests


# url = 'https://boston.craigslist.org/search/sof'
url = 'http://quotes.toscrape.com/'

# Requests from the url
response = requests.get(url)

# Status code 200 means successful request
print(response.status_code)

data = response.content

soup = BeautifulSoup(data, 'html.parser')

# for item in list(soup.children):
#     print(type(item))

# Tags within list
tags = list(soup.children)[-1]

# Identify Tags within list
for i in list(tags.children):
    type(i)

# Body within list
body = list(tags.children)[3]

# for i in body:
#     type(i)

# Drive into tags within body
body_tags = list(body.children)[1]

# for i in body_tags:
#     print(type(i))


inner_tags = list(body_tags.children)[3]
print(type(inner_tags))

# print(inner_tags)
for i in inner_tags.find_all('div', class_='quote'):
    print(i.find_all('div', class_='tags'))
    print('---')








