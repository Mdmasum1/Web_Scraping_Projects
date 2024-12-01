
# #Importing the necessary libraries
# import requests
# from bs4 import BeautifulSoup

# #Fetching the website
# base_url = "https://www.wiseradvisor.com/financial-advisors/alaska/ketchikan/rh-buchanan/2008584/"

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# }
# #Requesting the website
# response = requests.get(base_url, headers=headers)

# #Get the status code 
# #print(response.status_code)

# #page content
# page_content = response.text

# #Parsing the website and creating a BeautifulSoup object
# soup = BeautifulSoup(page_content, 'html.parser')

# #Html in a readable format
# #print(soup.prettify())

# #I need you to scrape the name, address and contact information for the advisor in the directory.
# #here is tag for the name "<a href="http://www.rhbuchanan.com" rel="nofollow" target="_blank" style="color: #00b0f0;  text-decoration: none !important; line-height: 30px;">RH BUCHANAN</a>"
# #under h1 tag"
# # # Locate <h1> tag and then the <a> inside it
# name = soup.find('h1').find('a').getText(strip=True)
 
# #print(name)

# #Extract the phone number
# #'
# '''  
#   <div style=" margin: 10px 0px 18px"> 
#   <div>Tel:  (907) 225-0833</div>
#     29 Main Street
#     <br>Suite 202<br>
#     <span>Ketchikan, Alaska </span>&nbsp;<span>99901</span>		
# </div>

# '''

# # Locate the div tag with the phone number
# telephone = soup.find('div', style=' margin: 10px 0px 18px').find('div').getText(strip=True)

# #Street adress only 
# ''' 
# # <div style=" margin: 10px 0px 18px"> 
#   <div>Tel:  (907) 225-0833</div>
#     29 Main Street"
# '''

# # Extract address details

# # Extract the street address using the <div> containing the full address
# address_div = soup.find('div', style=" margin: 10px 0px 18px")  # Locate the main address <div>
# address_parts = list(address_div.stripped_strings)  # Extract all strings and clean whitespace
# street = address_parts[1]  # Second item contains the street address
# suite = address_parts[2]  # Third item contains the suite number

# '''
#  <div style=" margin: 10px 0px 18px"> 
#   <div>Tel:  (907) 225-0833</div>
#     29 Main Street
#     <br>Suite 202<br>
#     <span>Ketchikan, Alaska </span>&nbsp;<span>99901</span>		
# </div>


# '''
# #based on the above code, the city and state are in the span tag
# # Extract the city and state
# city_state = address_div.find_all('span')[0].getText(strip=True)

# # Extract the ZIP code
# zip_code = address_div.find_all('span')[1].getText(strip=True)


# print(f"Name: {name}")
# print(f"Telephone: {telephone}")
# print(f"Street: {street}")
# print(f"Suite: {suite}")
# print(f"City, State: {city_state}")
# print(f"ZIP Code: {zip_code}")
####################################################


# Importing the necessary libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetching the website
base_url = "https://www.wiseradvisor.com/financial-advisors/alaska/ketchikan/rh-buchanan/2008584/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Requesting the website
response = requests.get(base_url, headers=headers)
page_content = response.text

# Parsing the website and creating a BeautifulSoup object
soup = BeautifulSoup(page_content, 'html.parser')

# Extracting details
name = soup.find('h1').find('a').getText(strip=True)
telephone = soup.find('div', style=' margin: 10px 0px 18px').find('div').getText(strip=True)
address_div = soup.find('div', style=" margin: 10px 0px 18px")
address_parts = list(address_div.stripped_strings)
street = address_parts[1]
suite = address_parts[2]
city_state = address_div.find_all('span')[0].getText(strip=True)
zip_code = address_div.find_all('span')[1].getText(strip=True)

# Prepare data for CSV
data = {
    'Name': [name],
    'Telephone': [telephone],
    'Street': [street],
    'Suite': [suite],
    'City, State': [city_state],
    'ZIP Code': [zip_code]
}

# Create a DataFrame using pandas
df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
output_file = "financial_advisor_data.csv"
df.to_csv(output_file, index=False)

print(f"Data saved to {output_file}")






























