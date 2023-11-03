#Project 2:Web Scraper using BeautifulSoup4 and Requests

import requests  #responsible for getting Web page content
from bs4 import BeautifulSoup #responsible for parsing html code

#get content from one page
url="https://books.toscrape.com/catalogue/page-1.html"

response=requests.get(url)#get information from url
response=response.content

print(response)

soup=BeautifulSoup(response,'html.parser')
print(soup)
ol=soup.find('ol')

articles=ol.find_all('article',class_='product_pod')
articles

#Get cointent of 50 books

books=[]
for i in range(1,51):
    url=f"https://books.toscrape.com/catalogue/page-{i}.html"  #to get content of 50 pages
    response=requests.get(url)#get information from url
    response=response.content
    soup=BeautifulSoup(response,'html.parser')
    ol=soup.find('ol')
    articles=ol.find_all('article',class_='product_pod')
    for article in articles:
        image=article.find('img')
        title=image.attrs['alt']
        star=article.find('p')
        star=star['class'][1]
        price=article.find('p',class_='price_color').text
        price=float(price[1:])
        books.append([title,price,star])

#for better view of alla the details we are viewing our data in csv file
import pandas as pd

#to view details in the csv file
df=pd.DataFrame(books,  columns=['Title','Price','Star Rating'])
df.to_csv('books.csv')
