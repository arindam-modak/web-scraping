def codeforces(username):
    head = 'http://codeforces.com/profile/'
    var = username
    URL = head + var
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')

    listRating = list(soup.findAll('div',class_="user-rank"))
    CheckRating = listRating[0].get_text()  #Check for rated or unrated
    if str(CheckRating) == '\nUnrated \n':
        # print('Not rated')
        out = 1000000
        return(out)
    else:
    # print('rated')
        listinfo = list((soup.find('div',class_="info")).findAll('li'))
        string = (listinfo[0].get_text())
        string = string.replace(" ","")
        str1,str2 = string.split('(')   # Well,.. don't judge me
        str3,str4 = str1.split(':') 
        out = int((str4.strip()))
        print(out)
        return(out)
