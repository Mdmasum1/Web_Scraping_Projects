import requests
from bs4 import BeautifulSoup

html_content = "https://www.myer.com.au/"
response = requests.get(html_content)

soup = BeautifulSoup(response.text, 'html.parser')
product_price = soup.find('p', class_='css-1ps1gwj')
print(product_price)