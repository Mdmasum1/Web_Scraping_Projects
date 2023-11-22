
from bs4 import BeautifulSoup
#import lxml

with open("website.html") as file:
    contents = file.read()


soup = BeautifulSoup(contents, "html.parser")

#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)

#Display the entire soup obbject
#Use prettify to have perfect indent
#print(soup.prettify())
#display all anchor <a > tags
#print(soup.a)
#print(soup.li)
#Pulls all of the pragraphs
#print(soup.p)
##Finding and selecting  particular element with ###
#Finding all anchor tag
all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)
#for tag in all_anchor_tags:
    #print(tag.getText())
    #print(tag.get("href"))

#when find or isolate specific attribute from whole program
heading = soup.find(name="h1", id="name")
#print(heading)
heading1 = soup.find(name="h3", class_="heading")
print(heading1)
#print(heading1.get("class"))







