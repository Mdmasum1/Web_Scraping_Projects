from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

def scrape_median_sale_prices_selenium(url):
    """
    Scrapes median sale prices using Selenium for JavaScript-rendered content.
    """
    # Set up Selenium WebDriver
    service = Service('/usr/local/bin/chromedriver')  # Replace with your ChromeDriver path
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Load the page
        driver.get(url)

        # Wait for the chart element to be present
        wait = WebDriverWait(driver, 10)
        chart_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@id, "medianSalePriceChart")]')))
        
        # Extract chart data
        chart_data = chart_element.get_attribute('data-chart-data')

        if chart_data:
            # Convert JSON chart data to a Pandas DataFrame
            import json
            data = json.loads(chart_data)
            df = pd.DataFrame(data['prices'])  # Adjust based on actual data structure
            return df
        else:
            print("Chart data not found!")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        driver.quit()

# Example Usage
if __name__ == "__main__":
    state = "TX"
    city = "Austin"
    base_url = f"https://www.redfin.com/city/30818/{state}/{city}/housing-market"
    df = scrape_median_sale_prices_selenium(base_url)
    if df is not None:
        print("Scraped Data:")
        print(df.head())
        df.to_excel("Median_Sale_Prices.xlsx", index=False)  # Save to Excel
