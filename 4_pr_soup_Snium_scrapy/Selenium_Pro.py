from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

# Path to ChromeDriver
chrome_driver_path = "/usr/local/bin/chromedriver"

# Chrome Options
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")  # Required for some environments
options.add_argument("--disable-dev-shm-usage")  # Overcome shared memory issues
options.add_argument("--disable-gpu")  # Optional
options.add_argument("--window-size=1920,1080")  # Optional for consistent layout

# ChromeDriver Service
service = Service(chrome_driver_path)

# WebDriver
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.audible.com/search")
    
    # Wait for the page to fully load by checking for specific elements
    wait = WebDriverWait(driver, 40)  # Increase timeout to 40 seconds
    
    # Wait for the container to be visible before interacting with it
    try:
        container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".adbl-impression-container.bc-container")))
    except TimeoutException:
        print("Timed out waiting for the container to be visible")
        driver.quit()
        exit()

    # Scroll down the page to trigger content loading
    for _ in range(3):  # Scroll 3 times
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for content to load after scrolling

    # Wait for the container to be fully loaded after scrolling
    try:
        container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".adbl-impression-container.bc-container")))
    except TimeoutException:
        print("Timed out waiting for the container to be visible after scrolling")
        driver.quit()
        exit()

    # Find all li elements inside the container using a more general XPath
    products = container.find_elements(By.XPATH, './/li')
    print(f"Total products found: {len(products)}")

finally:
    driver.quit()
