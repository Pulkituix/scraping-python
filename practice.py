import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=iphone&crid=2GO4I548Z5D4Z&sprefix=iphone%2Caps%2C220&ref=nb_sb_noss_2"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())``