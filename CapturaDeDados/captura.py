import urllib.request

from bs4 import BeautifulSoup

repo = "https://github.com/Adeilsoara?tab=repositories"

page = urllib.request.urlopen(repo)

soup = BeautifulSoup(page, 'html5lib')
# print(soup.title)
# print(soup.title.string)
todos_links = soup.find_all('a')
for link in todos_links:
    print(link.get('href'))


# list_item = soup.find('a', attrs={'itemprop': 'name codeRepository'})
# name = list_item.text.strip()
#print(name)