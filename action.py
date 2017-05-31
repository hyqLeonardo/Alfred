import voice
from info import *	# all personal information

import os
from datetime import datetime
import subprocess	# for shell commands
import webbrowser	# open browser
# another way of control browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# to send email
import smtplib
from email.mime.text import MIMEText


# set environment for chromedriver
chromedriver = "/media/ethan/Docs/projects/Alfred/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
# set environment for webbrowser
browser = webbrowser.get('google-chrome')

## Alfred's services
def open_web(website):
	browser.open_new_tab(website)

def search_web(content):
	website = 'http://www.google.com/search?btnG=1&q=%s' % content
	browser.open_new_tab(website)	

def open_selen(website):
	driver = webdriver.Chrome(chromedriver)
	driver.get(website)
	time.sleep(3)

def search_selen(website, content):
	driver = webdriver.Chrome(chromedriver)
	driver.get(website)
	search_box = driver.find_element_by_name('q')
	search_box.send_keys(content)
	search_box.submit()
	time.sleep(3)

# push project to github
def git_push(project):
	subprocess.call(['./script/git_push.sh', project])	

# record emial message to a text file in ./temp
def record_email():

	text = voice.listen()
	txtfile = './temp/email_' + (str(datetime.now())[:-10].replace(' ', '-'))
	fb = open(txtfile, 'w+')
	fb.write(text)
	fb.close()

# send recorded email
def send_email(subject, target):

	# Open a plain text file for reading.  For this example, assume that
	# the text file contains only ASCII characters.
	txtfile = './temp/email_' + (str(datetime.now())[:-10].replace(' ', '-'))
	fd = open(txtfile, 'rb')
	# Create a text/plain message
	msg = MIMEText(fd.read())
	fd.close()

	# me == the sender's email address
	# you == the recipient's email address
	if target != 'work':	# personal email
		me = PERSONAL_EMAIL
		dest = EMAIL_TARGET[target]
		msg['Subject'] = subject
		msg['From'] = me
		msg['To'] = ','.join(dest)
		# Send the message via SMTP server, with login, but don't include the
		# envelope header.
		server = smtplib.SMTP(PERSONAL_EMAIL_HOST)
		server.login(PERSONAL_EMAIL[:-8], PERSONAL_EMAIL_PASS)
	else:
		me = WORK_EMAIL
		dest = EMAIL_TARGET[target]
		msg['Subject'] = subject
		msg['From'] = me
		msg['To'] = dest
		# Send the message via SMTP server, with login, but don't include the
		# envelope header.
		server = smtplib.SMTP(WORK_EMAIL_HOST)
		server.login(WORK_EMAIL[:-8], WORK_EMAIL_PASS)
	print me
	print dest
	server.sendmail(me, dest, msg.as_string())
	server.quit()
