from util import *	# helper routines
from info import *	# all personal information
import voice
import vision

import subprocess	# for shell commands
import google
import smtplib
from email.mime.text import MIMEText

## Alfred's services

# control mouse and keyboard using gesture (camera required)
def control():
	pass

# search google and open links
class SearchGoogle:

	def __init__(self, query):
		self.query = query	# search query
		self.website = 'http://www.google.com/search?btnG=1&q=%s' % query
		self.search_ans = ''
		self.fetched_url = ''
		self.page_num = 3	# hard code this first

	# convinient to run parallel in search_web()
	def get_ans(self):
		self.search_ans = voice.listen()

	# convinient to run parallel in search_web()
	def fetch_url(self):
		self.fetched_url = google.search(self.query, stop = 5)

	def open_web(self, url):
		browser.open(url)

	def open_page(self):
		if 'yes' in self.search_ans or 'sure' in self.search_ans:	# open first (num) urls
			print 'ok'
			for url in self.fetched_url:
				if self.page_num > 0:	
					self.open_web(url)
				else:
					break
				self.page_num -= 1	# pages left
		else:
			pass

	# search, then open links
	def search_web(self):
		search_funcs = [self.get_ans, self.fetch_url, self.open_page]
		self.open_web(self.website)
		print 'Interested in some results?'
		# listen voice and search web running in parallel, p1 finish before p2
		run_parallel(search_funcs)
		print 'What now ?'
		control_ans = voice.listen()
		print control_ans
		if 'leave it to me' in control_ans:
			gesture_control()

# push project to github
def git_push(project):
	if OS == 'linux':
		subprocess.call(['./script/git_push.sh', project])
	elif OS == 'win':
		# subprocess.Popen('git_push.bat', cwd='D:\\projects\\alfred\\script')
		batch_path = 'D:/projects/alfred/script/git_push.bat'
		p = subprocess.Popen([batch_path, project])

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

