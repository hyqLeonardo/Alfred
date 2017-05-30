import os
import webbrowser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# set environment for chromedriver
chromedriver = "/media/ethan/Docs/projects/Alfred/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
# set environment for webbrowser
browser = webbrowser.get('google-chrome')

## Alfred's services
def open_web(website):
	browser.open_new_tab(website)

def open_selen(website):
	driver = webdriver.Chrome(chromedriver)
	driver.get(website)
	time.sleep(3)

def search_web(content):
	website = 'http://www.google.com/search?btnG=1&q=%s' % content
	browser.open_new_tab(website)	

def search_selen(website, content):
	driver = webdriver.Chrome(chromedriver)
	driver.get(website)
	search_box = driver.find_element_by_name('q')
	search_box.send_keys(content)
	search_box.submit()
	time.sleep(3)


# class (unittest.TestCase):
#     def setUp(self):
#         self.browser = webdriver.Chrome(chromedriver)

#     def tearDown(self):
#         self.browser.quit()

#     def test_open_facebook_and_login(self):

#         self.browser.get('https://www.google.com')
#         time.sleep(10)
		# username_field = self.browser.find_element_by_name('email')
		# password_field = self.browser.find_element_by_name('pass')

		# username_field.send_keys('TYPE_USERNAME_HERE')
		# password_field.send_keys('TYPE_PASSWORD_HERE')
		# password_field.send_keys(Keys.RETURN)
