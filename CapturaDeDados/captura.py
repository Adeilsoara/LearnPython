import urllib.request

from bs4 import BeautifulSoup

wiki = "https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil"

page = urllib.request.urlopen(wiki)

soup = BeautifulSoup(page, 'html5lib')
# print(soup.title)
# print(soup.title.string)
list_item = soup.find('li', attrs={'class': 'toclevel-1 tocsection-5'})
name = list_item.text.strip()
print(name)