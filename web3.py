import bs4 as bs
import urllib.request

url = input('enter - ')
sauce = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce,'lxml')     # lxml is a parser
print(soup.title)
print()
print(soup.title.name)
print()
print(soup.title.text)
print()
print(soup.title.string)
print()
print(soup.p)
print()
for para in soup.find_all('p'):
    print(para.text)
print()

print(soup.get_text())

for url in soup.find_all('a'):
    print(url.get('href'))


