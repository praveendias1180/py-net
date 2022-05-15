import requests

from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=Python'
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

tags = soup('h3')
for tag in tags:
    print(tag.find('div').text)