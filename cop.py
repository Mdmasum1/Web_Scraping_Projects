
import requests
from bs4 import BeautifulSoup

# Step 2: Fetch the webpage content
url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
web_content = response.text

# Step 3: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(web_content, 'html.parser')

# Step 4: Extract the movie titles
# The titles are within <h3> tags with class 'title'
titles = soup.find_all(name='h3', class_='title')

# Step 5: Print the top 100 movie titles
for i, title in enumerate(titles[:100], start=1):
    print(f"{i}. {title.get_text(strip=True)}")
