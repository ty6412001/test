
from splinter import Browser
from selenium import webdriver
from selenium.common.exceptions import TimeoutException


browser = Browser()
url = "http://www.meizitu.com"
browser.visit(url)
browser.find_by_id('picture').first.click()

if browser.is_text_present('splinter.cobrateam.info'):
    print "Yes, the official website was found!"
else:
    print "No, it wasn't found... We need to improve our SEO techniques"

#browser.quit()