
#Importing the necessary libraries
import requests
from bs4 import BeautifulSoup

#Fetching the website
base_url = "https://www.wiseradvisor.com/financial-advisors/alaska/ketchikan/rh-buchanan/2008584/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
#Requesting the website
response = requests.get(base_url, headers=headers)

#Get the status code 
#print(response.status_code)

#page content
page_content = response.text

#Parsing the website and creating a BeautifulSoup object
soup = BeautifulSoup(page_content, 'html.parser')

#Html in a readable format
#print(soup.prettify())

#I need you to scrape the name, address and contact information for the advisor in the directory.
#here is tag for the name "<a href="http://www.rhbuchanan.com" rel="nofollow" target="_blank" style="color: #00b0f0;  text-decoration: none !important; line-height: 30px;">RH BUCHANAN</a>"
#under h1 tag"
# # Locate <h1> tag and then the <a> inside it
name = soup.select_one("h1 a").text
 
print(name)
