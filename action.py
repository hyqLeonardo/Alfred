from util import *	# helper routines
from info import *	# all personal information
import voice

import subprocess	# for shell commands
import google
import smtplib
from email.mime.text import MIMEText

## Alfred's services
# search google and open links
class SearchGoogle:

	def __init__(self, query):
		self.query = query	# search query
		self.website = 'http://www.google.com/search?btnG=1&q=%s' % query
		self.search_ans = ''
		self.fetched_url = ''

	# convinient to run parallel in search_web()
	def get_ans(self):
		self.search_ans = voice.listen()

	# convinient to run parallel in search_web()
	def fetch_url(self):
		self.fetched_url = google.search(self.query, stop = 5)

	def open_web(self, url):
		browser.open(url)

	# search, then open links
	def search_web(self):
		search_funcs = [self.fetch_url, self.get_ans]
		self.open_web(self.website)
		print 'Interested in some results?'
		# listen voice and search web running in parallel, p1 finish before p2
		run_parallel(search_funcs)
		print self.search_ans
		for i in range(2):
			print self.fetched_url[i]
		if 'yes' in self.search_ans or 'sure' in self.search_ans:	# open first (num) urls
			print 'ok'
			num = 3	# let's hard code this first
			for url in self.fetched_url:
				if num > 0:	
					self.open_web(url)
				else:
					break
				num -= 1	# pages left
		else:
			print 'someting is wrong'

# def open_selen(website):
# 	driver = webdriver.Chrome(chromedriver)
# 	driver.get(website)
# 	time.sleep(3)

# def search_selen(website, query):
# 	driver = webdriver.Chrome(chromedriver)
# 	driver.get(website)
# 	search_box = driver.find_element_by_name('q')
# 	search_box.send_keys(query)
# 	search_box.submit()
# 	time.sleep(3)

# push project to github
def git_push(project):
	if OS == 'linux':
		subprocess.call(['./script/git_push.sh', project])
	elif OS == 'win':
		# subprocess.Popen('git_push.bat', cwd='\script')
		subprocess.call(['/script/git_push.bash', project])	

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

def gesture():
	pass