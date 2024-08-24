import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = "https://www.myer.com.au/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# # Print the title of the page
# print(soup.title)

# # Print the title of the page
# print(soup.title.text)

# # Print the first paragraph of the page
# print(soup.p.text)

# # Print all the links on the page
# links = soup.find_all('a')
# print(links)

# # Print the text of all the links on the page
# for link in links:
#     print(link.text)

# # Print the text of all the links on the page
# for link in links:
#     print(link.get('href'))

#print all the product-prince-now from the link
product_price = soup.find_all('p', class_='css-1mxfaop')
for price in product_price:
    print(price.text)


# # /populate the price and brand in a dictionary
# # #############################################
# products = []
# for i in range(len(brand)):
#     product = {
#         'brand': brand[i].text,
#         'price': price[i].text
#     }
#     products.append(product)
# print(products)












#############################################
# a_tags = soup.find_all('a')

# for a in a_tags:
#     print("Brand: ",  a.text)


# Output:  https://www.myer.com.au/

