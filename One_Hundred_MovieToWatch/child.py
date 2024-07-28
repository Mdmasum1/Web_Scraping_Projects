
#If you want to find only descendants that are children, you can use 
#the .children tag:

import requests
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/page3.html'
response = requests.get(url)
html = response.text
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table', {'id' : 'giftList'}). children:
    print(child)


