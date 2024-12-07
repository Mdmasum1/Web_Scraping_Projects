
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# URL to scrape
url = 'https://www.audible.com/search'

# Path to ChromeDriver
chrome_driver_path = '/usr/local/bin/chromedriver'

# Create a Service object
service = Service(chrome_driver_path)

# Configure Chrome options
options = Options()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument('--no-sandbox')  # Prevent sandbox issues
options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
options.add_argument('--disable-gpu')  # Disable GPU acceleration (optional for headless)

# Initialize the WebDriver with options and service
driver = webdriver.Chrome(service=service, options=options)

# Open the web page
driver.get(url)
driver.maximize_window()


container = driver.find_element_by_class_name('adbl-impression-container')
products = container.find_elements_by_xpath('./li')

for product in products:
    
# Print the page title
#print("Page title is:", driver.title)

# Close the browser
#driver.quit()
