
#If you want to find only descendants that are children, you can use 
#the .children tag:

# import requests
# from bs4 import BeautifulSoup

# url = 'http://www.pythonscraping.com/pages/page3.html'
# response = requests.get(url)
# html = response.text
# bs = BeautifulSoup(html, 'html.parser')

# for child in bs.find('table', {'id' : 'giftList'}). children:
#     print(child)

#**************************************************************
#The solution is to look for something identifying about the tag itself.
#In this case, you can look at the file path of the product 
#imgages
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3/html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('imag', 
                     {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})


for image in images:
    print(image['src'])

'''
 ---This prints only the relative image paths that start with 
 ../img/gifts/img and end in .jpg, the output of which is the 
 following :
../img/gifts/img1.jpg
 ../img/gifts/img2.jpg
 ../img/gifts/img3.jpg
 ../img/gifts/img4.jpg
 ../img/gifts/img6.jpg

##A regular expresion can be inserted as any argument in a BeautifulSoup
 expression, allowing you a great deal of flexibility in finding target
 elements
 
'''

















