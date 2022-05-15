import requests

from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=Python'
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

headings = soup('h3')
for heading in headings:
    print(heading.find('div').text)
    print(heading.parent.get('href'))