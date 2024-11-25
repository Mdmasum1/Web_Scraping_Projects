
from bs4 import BeautifulSoup
import requests

#chromedriver_path = '/workspaces/Web_Scraping_Projects/chromedriver"
website = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

#Beautiful Soup: Steps before scraping a website
#1)Fetch the pages(obtained a resonse object)
result = requests.get(website)

#2) Page content
content = result.text 

#3) Create soup
soup = BeautifulSoup(content, "html.parser")

print(soup.prettify())

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
