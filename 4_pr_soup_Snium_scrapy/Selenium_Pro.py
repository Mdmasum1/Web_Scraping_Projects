
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service

url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

# Replace with the actual path to ChromeDriver
#chrome_driver_path = '/workspaces/Web_Scraping_Projects/chromedriver'

# Create a Service object
#service = Service(chrome_driver_path)
driver = webdriver.Chrome(executable_path='/workspaces/Web_Scraping_Projects/chromedriver')

#Open a web page 
driver.get(url)

#print the page title
print(driver)

#Close the browser
driver.quit()
