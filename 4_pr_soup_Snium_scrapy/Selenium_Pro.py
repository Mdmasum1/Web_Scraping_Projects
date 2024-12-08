from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Path to ChromeDriver
chrome_driver_path = "/usr/local/bin/chromedriver"

# Chrome Options
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")  # Required for some environments
options.add_argument("--disable-dev-shm-usage")  # Overcome shared memory issues
options.add_argument("--disable-gpu")  # Optional
options.add_argument("--window-size=1920,1080")  # Optional for consistent layout
options.binary_location = "/usr/bin/google-chrome"  # Set binary location if needed

# ChromeDriver Service
service = Service(chrome_driver_path)

# WebDriver
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.audible.com/search")
    driver.maximize_window()
finally:
    driver.quit()
