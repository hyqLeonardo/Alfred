
import os
import sys
from datetime import datetime
from multiprocess import Process	# for multi process running parallel
import webbrowser	# open browser

# get operating system
OS = ''
if sys.platform == 'linux' or sys.platform == 'linux2':
	OS = 'linux'
elif sys.platform == 'win32':
	OS = 'win'
else:
	print 'What is this operating system?'

# # another way of control browser
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# to send email

# # set environment for chromedriver
# chromedriver = "/media/ethan/Docs/projects/Alfred/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver

# set environment for webbrowser
if OS == 'linux':
	browser = webbrowser.get('google-chrome')
elif OS == 'win':
	# have to use linx path style
	browser = webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s')
else:
	print 'What is this operating system?'

# enable functions run in parallel, priority ordered as fns order
def run_parallel(funcs):
	proc = []
	for func in funcs:
		p = Process(target = func)
		p.start()
		proc.append(p)
	for p in proc:
		p.join()

