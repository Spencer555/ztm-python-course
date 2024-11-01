from selenium import webdriver
from selenium.webdriver.common.by import By
import time 



chrome_browser = webdriver.Chrome()

# maximize
chrome_browser.maximize_window()

# open a site 
chrome_browser.get('https://www.google.com')

print('gog', 'Google' in chrome_browser.title)
print('gogrre', chrome_browser.find_element(By.CLASS_NAME, "bto"))


button = chrome_browser.find_element(By.CLASS_NAME, "gNO89b")
print(button.get_attribute('innerHTML'))
# print(chr)


time.sleep(1)
print('button', chrome_browser.body)

'''
we can grab items by 
by class name 
tag name 
link text
partial link text
xpath

find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")
'''


# open google enter google text and search
# buttons = chrome_browser.find_element(By.CLASS_NAME, "gNO89b")

# if 'Google Search' in buttons:
#     buttons.click()
#     time.sleep(10)



