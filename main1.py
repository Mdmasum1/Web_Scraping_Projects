
from bs4 import BeautifulSoup

import requests

#part 375: Scraping from live website
response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
#print(soup.title)
articles = soup.find_all(name="a", rel = "noreferrer")

#when we find all of the article from the page 
# we need to use for loop instead of single variable
article_texts = []
article_links = []
for article_tag in articles:
   text = article_tag.getText()
   article_texts.append(text)
   link = article_tag.get("href")
   article_links.append(link)

#use comprehension list
article_upvotes =[int(score.getText().split()[0]) for score in soup.find_all(name="span", class_ = "score")]

largest_number = max(article_upvotes)

#We can find the lagest number index
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])



#print out that holds the largest number of upvotes
#print(largest_number)

# print(article_texts)
# print(article_links)
# #This is the method how you can hold the number from upvotes
# print(article_upvotes)

# #import lxml

# with open("website.html") as file:
#     contents = file.read()


# soup = BeautifulSoup(contents, "html.parser")

# #print(soup.title)
# #print(soup.title.name)
# #print(soup.title.string)

# #Display the entire soup obbject
# #Use prettify to have perfect indent
# #print(soup.prettify())
# #display all anchor <a > tags
# #print(soup.a)
# #print(soup.li)
# #Pulls all of the pragraphs
# #print(soup.p)
# ##Finding and selecting  particular element with ###
# #Finding all anchor tag
# all_anchor_tags = soup.find_all(name="a")
# #print(all_anchor_tags)
# #for tag in all_anchor_tags:
#     #print(tag.getText())
#     #print(tag.get("href"))

# #when find or isolate specific attribute from whole program
# heading = soup.find(name="h1", id="name")
# #print(heading)
# heading1 = soup.find_all(name="h3", class_="heading")
# print(heading1)
# #print(heading1.get("class"))

# #company_url = soup.select_one(selector="p a")
# name = soup.select_one(selector="#name")
# print(name)
# #print(company_url)
# headings = soup.select(".heading")
# print(headings)




