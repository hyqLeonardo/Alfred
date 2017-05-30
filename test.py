# -*- coding: utf-8 -*-

import time
import os
import webbrowser
# from selenium import webdriver

# # driver = webdriver.Chrome("~/Downloads/chromedriver")  # Optional argument, if not specified will search path.
# chromedriver = "/media/ethan/Docs/projects/Alfred/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chromedriver)

# driver.get('http://www.google.com');
# search_box = driver.find_element_by_name('q')
# search_box.send_keys("网易云音乐".decode('utf-8'))
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()

url = "www.google.com"
b = webbrowser.get('google-chrome')
b.open(url)