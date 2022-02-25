import urllib.request

from bs4 import BeautifulSoup

wiki = "https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil"

page = urllib.request.urlopen(wiki)

soup = BeautifulSoup(page, 'html5lib')

list_item = soup.find('li', attrs={'class': 'toclevel-2 tocsection-26'})
name = list_item.text.strip()
print(name)