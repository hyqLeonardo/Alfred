# -*- coding: utf-8 -*-
import os
import sys
import voice
import action

def follow_up():

	text = voice.listen()

	if text == 'well done' or text == 'good job':
		sys.exit(0)
	if 'leave it to me' in text:
		action.gesture()


def alfred():

	print 'How can I help you, Sir'
	text = voice.listen()

	if text == 'play me some music':	# play music
		action.open_web('http://music.163.com/')
	elif 'search' in text:	# search google
		query = text.replace('search ', '')
		s = action.SearchGoogle(query)
		s.search_web()
		follow_up()
	elif 'push project' in text:	# push project to github
		action.git_push(text.replace('push project ', ''))
	elif 'update yourself' in text:
		action.git_push('alfred')
	elif 'send email to' in text:	# auto send email
		subject = 'auto send'
		target = text.replace('send email to ', '')
		action.record_email()
		action.send_email(subject, target)
	elif 'well done' in text or 'good job' in text:
		sys.exit(0)
		# return 
	elif "let's call it a day" in text:
		os.system('shutdown')
	else:
		print 'Pardon, sir'

# daemon always on
def daemon():

	text = voice.listen()

	if text == None:
		return
	if 'alfred' in text:	# wake up Alfred
		alfred()

if __name__ == '__main__':

	while(True):
		daemon()
	# search = action.SearchGoogle("product manager")
	# search.search_web()
