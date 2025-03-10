# Alex Miller
# 12 - Web Scraping

# webbrowser == opens a browser to a specific page
# requests == downloads files and web pages
# bs4 == parses HTML
# selenium == lauches and controls a web browser, able to fill in forms and simulate mouse clicks in this browser

import webbrowser
webbrowser.open('https://google.com')

# Downloading Files From the Web with the Requests Module

import requests 

# Downloading a Web Page with the requests.get() function

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
print(res.status_code == requests.codes.ok) # checking if the request of the web page succeeded, status code for 'OK' is 200, like 404 = 'Not Found'
print(len(res.text)) # if requests succeeded the download web page is then stored into the text attribute of the response object
print(res.text[:250]) # displays the first 250 characters

print()

# Checking for Errors


res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status() # easier way to check if the request was successful, will raise exception if there was an error
except Exception as exc:
    print('There was a problem: %s' % (exc))

print()

# Saving Downloaded Files to Hard Drive

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb') # opens file in 'write binary' mode to maintain Unicode encoding of the text
for chunk in res.iter_content(100000): # 'iter_content' returns 'chunks' of the content through each iteration, each chunk is in bytes which you can specify the amount
    playFile.write(chunk) # write the chunk to the file

playFile.close()

print()

# write() returns the number of bytes written to the file
# requests.get() == download file
# open('', 'wb') == create a new file in write binary mode
# loop over the Response object's iter_content() method
# write() on each iteration to write the content to the file
# close() == closes the file

#  Creating a BeautifulSoup Object from HTML

import bs4

res = requests.get('https://nostarch.com') # download page
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser') # passes text attribute of the response to bs4, returns bs4 object that is then stored in a variable
print(type(noStarchSoup))

print()

# once you have the beautifulsoup object you can then use it to find specific elements in an html document

# Finding an Element With the select() Method

# you can call the select() method on a bs4 object and pass a string of a CSS selector for the element you are looking for

# most common:

# soup.select('div') == all elements named <div>
# soup.select('#author') == all elements with id attribute of 'author'
# soup.select('.notice') == all elements that use a CSS class atribute named 'notice'
# soup.select('div span') == all elements named <span> that are within an element named <div>
# soup.select('div > span') == all elements named <span> that are directly within an element named <div>, nothing inbetween
# soup.select('input[name]') == all elements named <input> that have a name attribute of any value
# soup.select('input[type="button"]') == all elements named <input> that have an attribute named 'type' with the value of 'button'

# the select() method returns a list of 'Tag' objects, which can be passed to the str() to show the HTML tags they represent, Tag values also have an 'attrs' attribute that shows all the HTML attributes of the tag as a dictionary

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
print(type(elems)) # elems is a list of Tag objects
print(len(elems)) # 1
print(type(elems[0])) # <class 'bs4.element.Tag'>
print(str(elems[0])) # <span id="author">Al Sweigart</span>
print(elems[0].getText()) # 'Al Sweigart'
print(elems[0].attrs) # {'id': 'author'}

print()

pElems = exampleSoup.select('p') # getting a list of all elements that are 'p'
print(str(pElems[0])) # <p>Download my <strong>Python</strong> book from <a href="inventwithpython.com">my website</a></p>
print(pElems[0].getText()) # 'Download my Python book from my website'
print(str(pElems[1])) # <p class="slogan">Learn Python the easy way!</p>
print(pElems[1].getText()) # 'Learn Python the easy way!'
print(str(pElems[2])) # <p>By <span id="author">Al Sweigart</span></p>
print(pElems[2].getText()) # 'By Al Sweigart'

print()

# Getting Data from Element's Attributes

# get() for Tag objects makes is simple to get attribute values, pass a string of an attribute name and returns that value

soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanElem = soup.select('span')[0]
print(str(spanElem)) # <span id="author">Al Sweigart</span>
print(spanElem.get('id')) # 'author'
print(spanElem.get('some_nonexistend_addr') == None) # True
print(spanElem.attrs) # {'id': 'author'}

print()

# Selenium

from selenium import webdriver
browser = webdriver.Firefox()
# browser.get('https://inventwithpython.com')

'''
try:
    elem = browser.find_element_by_class_name('jumbotron')
    print('found <%s> element with that class name!' % (elem.tag_name))
except:
    print('was not able to find an element with that name')

'''

# Finding Elements on the Page

# elements(s) == both 'element' and 'elements'

# browser.find_element(s)_by_class_name(name) == elements that use the CSS class 'name'
# browser.find_element(s)_by_css_selector(selector) == elements that match the CSS 'selector'
# browser.find_element(s)_by_id(id) == elements that match the 'id' attribute value
# browser.find_element(s)_by_link_text(text) == <a> elements that completely match the 'text' provided
# browser.find_element(s)_by_partial_link_text(text) == <a> elements that contain the 'text' provided
# browser.find_element(s)_by_name(name) == elements with a matching 'name' attribute value
# browser.find_element(s)_by_tag_name(name) == elements with a matching tag 'name' (case insensitive, an <a> element is matched by 'a' and 'A') == only one case insensitive

# WebElement Objects

# tag_name == the tag name, ex: a for <a>
# get_attribute(name) == the value for the elements 'name' attribute
# text == the text within the element, ex: 'hello' in <span>hello</span>
# clear() == for text field or text area elements, clears the text typed into it
# is_displayed() == returns True if the element is visible, False if not
# is_enabled() == for input elements, returns True if the element is enabled, False if not
# is_selected() == for checkbox or radio button elements, returns True if element is selected, False if not
# location == a dictionary with keys, x and y position of the element on the page

print()

# Clicking the Webpage
'''

linkElem = browser.find_element_by_link_text('Read Online for Free')
print(type(linkElem)) # <class 'selenium.webdriver.remote.webelement.FirefoxWebelement'>
linkElem.click() # clicks the link

'''

# Filling Out and Submitting Forms

'''

browser.get('https://login.metafilter.com')
userElems = browser.find_element_by_id('user_name')
userElems.send_keys('YourUsername')
passwordElem = browser.find_element_by_id('user_pass')
passwordElem.send_keys('YourPassword')
passwordElem.submit()

'''

# Sending Special Keys

# Keys.DOWN, Keys.UP, Keys.RIGHT, Keys.LEFT == arrow keys
# Keys.ENTER, Keys.RETURN == Enter and Return keys
# Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP == home, end, pageup, and pagedown keys
# Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETS == esc, backspace, and delete keys
# Keys.TAB == tab key

# if the cursor is not currently in a text field, HOME and END keys scroll to the top and bottom of the page respectively

from selenium.webdriver.common.keys import Keys
browser.get('https://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END) # Scrolls to bottom
htmlElem.send_keys(Keys.HOME) # Scrolls to top

print()

# Clicking Browser Buttons

# browser.back() == back button
# browser.forward() == forward button
# browser.refresh() == refresh button
# browser.quit() == close window button