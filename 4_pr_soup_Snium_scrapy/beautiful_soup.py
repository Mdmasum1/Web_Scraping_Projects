
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# # Set up Chrome WebDriver
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run browser in headless mode
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# service = Service('/usr/local/bin/chromedriver')  # Update with the path to your chromedriver
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # Open the website
# website = 'https://subslikescript.com/movies'
# driver.get(website)

# # Get page source after JavaScript execution
# content = driver.page_source

# # Use BeautifulSoup to parse
# from bs4 import BeautifulSoup
# import requests

# soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())

# driver.quit()


# #Finding element with Beautiful Soup
# # soup.find(id="specific_id")

# # #Taking two arguments
# # soup.find('tag', class_="class value")

# # #ex: tag is 'h1' here taking only one arguments
# # soup.find('tag')

# # #Fiding all elments with Beautiful Soup
# # #find_ll return list -->list = [a, b, c, d]

# # soup.find_all("h2")

#*********************************************
'''
'''
import cloudscraper
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()  # Creates a scraper that can bypass Cloudflare
#website = 'https://subslikescript.com/movie/Titanic-120338'

#Scraping the multiple links with the same pages
root = 'https://subslikescript.com'
website = f'{root}/movies'
response = scraper.get(website)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())
box = soup.find('article', class_='main-article')

links = []
#Looping through the each link from the article elements
for link in box.find_all('a', href=True):
    links.append(link['href']) #ppending the links to the list

print(links)

for link in links:
    website = f'{root}/{link}'
    response = scraper.get(website)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup.prettify())
    box = soup.find('article', class_='main-article')

        
    title = soup.find('h1').get_text()
    transcript = soup.find('div', class_='full-script').get_text(strip=True, separator=' ')
    #print(transcript)

    with open(f'{title}.txt', 'w') as file:
        file.write(transcript)


