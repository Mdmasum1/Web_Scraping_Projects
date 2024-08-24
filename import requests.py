import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://www.myer.com.au/"


response = requests.get(url)
# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

