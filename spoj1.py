import bs4 as bs
import urllib.request

url = input('enter spoj profile url - ')
sauce = urllib.request.urlopen(url).read()    
soup = bs.BeautifulSoup(sauce,'lxml')     # lxml is a parser
#print(soup)

info = (soup.find_all('p'))
for i in info:
    print(i.text)

no_of_questions = int(soup.find('dd').text)
print(" no. of questions = ",no_of_questions)

