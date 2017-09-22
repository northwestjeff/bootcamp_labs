import bs4 as bs
import urllib.request

source = urllib.request.urlopen("https://azcookbook.com").read()
soup = bs.BeautifulSoup(source, 'html.parser')

for body in soup.find_all('body'):
    print(body)
    print("================")


