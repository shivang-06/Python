import urllib.request as url
import bs4


name=input("Enter the movie name: ")
name=name.split()
name='+'.join(name)
http=url.urlopen('https://www.imdb.com/find?ref_=nv_sr_fn&q='+ name)

page=bs4.BeautifulSoup(http,'lxml')
element=page.find('td', class_="result_text")
a_tag=element.find('a')
href=a_tag['href']

path="https://imdb.com"+href
http=url.urlopen(path)
page=bs4.BeautifulSoup(http,'lxml')
title=page.find('div',class_="title_wrapper")
title=title.text.replace('\n','')
title=' '.join(title.split())
print(title)

print('''

What do you want see ?
1. Movie Rating                 2. Movie Reviews
''')
choice=int(input("Enter your choice: "))

if choice==1:
    title=page.find('div', class_='ratingValue')
    print("The Rating is -"+title.text)

elif choice==2:
    title=page.find('div',id="quicklinksMainSection")
    