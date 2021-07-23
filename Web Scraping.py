# importing a required packages
import requests 
import html5lib
from bs4 import BeautifulSoup

# give a url of website which one to scrape 
url = "https://codewithharry.com"
# r has all the html code 
r = requests.get(url)
# r returns response so if we want the code we write r.content
htmlContent = r.content
# printing the code
print(htmlContent)

# instead of content we can use text
htmlTexr = r.text
print(htmlTexr)

# traverse the html code 
url = "https://codewithharry.com"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
# to print html in tree structure 
print(soup.prettify)

# parsing the data from html webpage
soup = BeautifulSoup(r.content, 'html.parser')
print(soup)

# HTML tree traversal (targeting data)
url = "https://www.codewithharry.com/videos/python-web-scraping-tutorial-in-hindi"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
for i in soup.find_all("code"):
    #print(i.text)
    # we can also do it like this
     print(i.get_text())
     
     # extract title from web page = 
title = soup.title
print(title)

# find first paragraph tag of the webpage
print(soup.find('p'))

# find all the paragraph tags of the webpage
paras = soup.find_all('p')
print(paras)

for i in paras:
    print(i)
    
    # get the class of an elements
print(soup.find('p'),['class'])

# finding elements from class names
print(soup.find_all('p', class_='lead'))

print(soup.find_all('p',class_code="code-toolbar"))

# finding elements through elements id
print(soup.find(id='qna'))

# getting text from tags
head = soup.head
print(head.text)
# OR
div = soup.div
print(div.get_text)

# getting all the links 
anchors = soup.find_all('a')
print(anchors)

for i in paras:
    print(i('href'))
    
    for i in paras:
        print(i.get('href'))
        
# taking a html from a variable instead of requests
html = '''
<body>
<ul>
<li>This</li>
<li><a>This</a></li>
<li>This</li>
<li>This</li>
<li id="li">This</li>
<li> This </li>
</ul>
</body>
'''
soup = BeautifulSoup(html, 'html.parser')
print(html)

ul = soup.find("ul")
print(ul.contents)
# we can return a list which can iterate

# make a children class
ul = soup.find('ul')
for i in ul.children:
    print(i)
    
    # make a parent class 
ul = soup.find('ul')
print(ul.parent)

print(ul.parent.parent)

# next sibling or previous siblings
ul = soup.find(id='li')
print(ul.next_sibling.next_sibling)

ul = soup.find(id="li")
for j in ul.next_siblings:
    print(j)
    
    for i in ul.previous_siblings:
        print(i)


print(ul.previous_sibling.previous_sibling)


# stripped string
ul = soup.find(id = "li")
elem = ul.next_sibling.next_sibling
print(elem)
for i in elem.stripped_strings:
    print(i)
    
    
    # write a data in csv
f = open("file.csv", "w")
f.write("Every,word,will,go,in,separate,column\n")
f.write("This,will,go,in,next,row")
f.close()

with open("file.csv", "w") as f:
    f.write("Every,word,will,go,in,separate,column\n")
    f.write("This,will,go,in,next,row")
    
    # If you want to scrape a website:
# 1. Use the API
# 2. HTML Web Scraping using some tool like bs4

# Step 0: Install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Step 3: HTML Tree traversal
# 
# Commonly used types of objects:
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup
# # 4. Comment
# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))


# Get the title of the HTML page
title = soup.title

# Get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)

# print(anchors)

# Get first element in the HTML page
# print(soup.find('p') ) 

# Get classes of any element in the HTML page
# print(soup.find('p')['class'])

# find all the elements with class lead
# print(soup.find_all("p", class_="lead"))

# Get the text from the tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())

# Get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'): 
        linkText = "https://codewithharry.com" +link.get('href')
        all_links.add(link)
        # print(linkText)

navbarSupportedContent = soup.find(id='navbarSupportedContent')

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
# for elem in navbarSupportedContent.contents:
#     print(elem)
 
# for item in navbarSupportedContent.strings:
#     print(item)

# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# print(navbarSupportedContent.parent)
# for item in navbarSupportedContent.parents: 
#     print(item.name)

# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

# elem = soup.select('.modal-footer')
# print(elem)
elem = soup.select('#loginModal')[0] 
print(elem)