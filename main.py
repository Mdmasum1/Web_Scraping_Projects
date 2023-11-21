
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
print(soup.p)
