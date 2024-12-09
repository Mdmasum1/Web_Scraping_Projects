
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#url of the page we want to scrape
web ="https://www.amazon.com"

# Path to the chromedriver
path = "/usr/local/bin/chromedriver"

#create new instances of service
Service = Service(executable_path=path)

# Create a new instance of the Chrome driver as driver
driver = webdriver.Chrome(service=Service)

# Navigate to the page by driver
driver.get(web)

#quit driver
#driver.quit()