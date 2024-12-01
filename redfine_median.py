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
        #<div class="housingMarketDropdown" id="home_prices"><span class="field select Select withFlyout withOptions mounted clickable optional" data-rf-test-name="Select"><span data-rf-test-name="Select" class="input" role="listbox" tabindex="0"><span class="container"><span class="value">Median Sale Price</span><span class="arrow"><svg class="SvgIcon dropdown"><svg viewBox="0 0 10 10"><path d="M1.601 3h6.792a.25.25 0 01.177.427L5.174 6.823a.25.25 0 01-.354 0L1.424 3.427A.25.25 0 011.601 3"></path></svg></svg></span></span><select class="select" tabindex="-1"><option selected="" value="0" aria-label="Median Sale Price">Median Sale Price</option><option value="1" aria-label="# of Homes Sold"># of Homes Sold</option><option value="2" aria-label="Median Days on Market">Median Days on Market</option></select></span></span><span class="field select Select propertyTypeDropdown withFlyout withOptions mounted selected clickable optional" data-rf-test-name="Select"><span data-rf-test-name="Select" class="input" role="listbox" tabindex="0"><span class="container"><span class="value">All Home Types</span><span class="arrow"><svg class="SvgIcon dropdown"><svg viewBox="0 0 10 10"><path d="M1.601 3h6.792a.25.25 0 01.177.427L5.174 6.823a.25.25 0 01-.354 0L1.424 3.427A.25.25 0 011.601 3"></path></svg></svg></span></span><select class="select" tabindex="-1"><option selected="" value="All" aria-label="All Home Types">All Home Types</option><option value="6" aria-label="Single Family Homes">Single Family Homes</option><option value="13" aria-label="Townhouses">Townhouses</option><option value="3" aria-label="Condos/Co-ops">Condos/Co-ops</option></select></span></span></div>
        #show me the median sale price and Xpath
        #Xpath
        

        chart_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[(@id, "home-prices")]')))
        
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
