import requests
from bs4 import BeautifulSoup as bs

url = ("https://www.goodreads.com/review/list_rss/171499739?key=Q2SS70nHhSbpMIZdEDFXpoVzWuLSbnDn5-dyYwjGS1OO6Yzp&shelf=%23ALL%23")
harry = ("https://harrystenholm.github.io/main/")

pageharry = requests.get(harry)
blahharry = bs(pageharry.content, "html.parser")

#print(blahharry.h1)

page = requests.get(url)
tag = (page.title)

print(tag)


