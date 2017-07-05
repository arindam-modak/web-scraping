import requests
from bs4 import BeautifulSoup
import re

head = "http://codeforces.com/profile/"
var = str(input())
URL = head + var

page  = requests.get(URL)
soup = BeautifulSoup(page.content,'html.parser')

a = list(soup.findAll('li'))
print(a)
for i in a:
    if 'Contest rating:' in i:
        print(i)
        

