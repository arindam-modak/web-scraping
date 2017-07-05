import requests
from bs4 import BeautifulSoup
import re

head = "http://git-awards.com/users/"
var = input()
URL = head + var

page  = requests.get(URL)
soup = BeautifulSoup(page.content,'html.parser')
a = list(soup.findAll('div',class_='col-md-3 info'))
b = list(soup.findAll('td'))
lang=[]
f = 0
for i in a:
    c = i.text.lstrip().rstrip()
    if 'your ranking' in c and f==0:
        f=1
        continue
    if 'ranking' in c:
        s=""
        d = c.split(" ")
        for j in d:
            if j!="ranking":
                s+=j+" "
        lang.append(s.rstrip())
        
print(lang)
record = []
s=""
k=0
i=0
while(i<len(b)):
    c = b[i].text.lstrip().rstrip()
    if "We couldn't find your city from your location on GitHub" in c:
        s = "0-0-"
        s+= "Worldwide-"
        
        d = b[i+2].text.split("/")
        r1=""
        r2=""
        for j in d[0]:
            if j>='0' and j<='9':
                r1+=j
        for j in d[1]:
            if j>='0' and j<='9':
                r2+=j
        s+= r1 + "-" + r2 + "-"
        s+= "Repos-"
        s+= b[i+4].text.rstrip().lstrip()+"-"
        s+= "Stars-"
        s+= b[i+6].text.rstrip().lstrip()
        s = lang[k] + "-" + s
        record.append(s)
        k+=1
        i = i+7
    else:
        s = b[i].text + "-"
        d = b[i+1].text.split("/")
        r1=""
        r2=""
        for j in d[0]:
            if j>='0' and j<='9':
                r1+=j
        for j in d[1]:
            if j>='0' and j<='9':
                r2+=j
        s+= r1 + "-" + r2 + "-"
        s += b[i+2].text + "-"
        d = b[i+3].text.split("/")
        r1=""
        r2=""
        for j in d[0]:
            if j>='0' and j<='9':
                r1+=j
        for j in d[1]:
            if j>='0' and j<='9':
                r2+=j
        s+= r1 + "-" + r2 + "-"
        i = i+3
        s+= "Worldwide-"
        
        d = b[i+2].text.split("/")
        r1=""
        r2=""
        for j in d[0]:
            if j>='0' and j<='9':
                r1+=j
        for j in d[1]:
            if j>='0' and j<='9':
                r2+=j
        s+= r1 + "-" + r2 + "-"
        s+= "Repos-"
        s+= b[i+4].text.rstrip().lstrip()+"-"
        s+= "Stars-"
        s+= b[i+6].text.rstrip().lstrip()
        s = lang[k] + "-" + s
        record.append(s)
        k+=1
        i = i+7

print(record)
#s=""
#record=[]
#f=1
#for i in len(b):
    #c = b[i].text.lstrip().rstrip()
    #if f==0:
        #record.append(s)
        #f=1
    #for j in c and :
        
        
    
