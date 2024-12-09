
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# URL of the page we want to scrape
web = "https://www.amazon.com"

# Path to the chromedriver
path = "/usr/local/bin/chromedriver"

# Create a new instance of Options
chrome_options = Options()

# Create new instances of service
service = Service(executable_path=path)


# Create a new instance of the Chrome driver as driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the page
driver.get(web)

# Print the page title to verify
print("Page title is:", driver.title)

# Close the browser
driver.quit()
