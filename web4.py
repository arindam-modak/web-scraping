import bs4 as bs
import urllib.request

url = input('enter - ')
sauce = urllib.request.urlopen(url).read()    #'https://pythonprogramming.net/parsememcparseface/'
soup = bs.BeautifulSoup(sauce,'lxml')     # lxml is a parser

nav = soup.nav
#print (nav)
for url in nav.find_all('a'):
    print (url.get('href'))

body = soup.body
for para in body.find_all('p'):
    print (para.text)

for div in soup.find_all('div', class_='body'):
    print (div.text)
