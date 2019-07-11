from on import *
import requests
import bs4

banner()

res = requests.get('https://www.geeksforgeeks.org/data-structures/')

soup = bs4.BeautifulSoup(res.text,'lxml') # lxml specifies the parsing tree Syntactic analyzer
print(soup)



for i in soup.select('.entry-content'):
    print ( i.text )
    
# link :  https://en.wikipedia.org/wiki/Web_scraping
# class :  mw-headline '''
