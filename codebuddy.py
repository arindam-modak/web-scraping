import requests
from bs4 import BeautifulSoup

def codebuddy(username):
    URL = "https://codebuddy.co.in/ranks/practice"
    page  = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')
    table = list(soup.find_all('tr'))
    for i in table:
        parameters = list(i.find_all('label'))
        #print (i.find('label',class_="highlight").text)
        if str(parameters[1].text)==username:
            output = str(int(parameters[0].text))+" "+str(int(parameters[2].text))+" "+str(float(parameters[3].text))
            return (output)
    return (-1)

a = codebuddy("spectrum").split(" ")
print (a)
        

