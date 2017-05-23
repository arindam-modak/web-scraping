import bs4 as bs
import urllib.request

url = input('enter - ')
sauce = urllib.request.urlopen(url).read()    #'https://pythonprogramming.net/parsememcparseface/'
soup = bs.BeautifulSoup(sauce,'lxml')     # lxml is a parser

table = soup.table
table = soup.find('table')
print (table)

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print (row)
