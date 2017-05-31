# -*- coding: utf-8 -*-
import os
import sys
import voice
import action

def alfred():

	text = voice.listen()

	if text == 'play me some music':	# play music
		action.open_web('http://music.163.com/')
	elif 'search for' in text:	# search google
		action.search_web(text.replace('search for ', ''))
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
		print 'all right'
		sys.exit(0)
		# return 
	elif "let's call it a day" in text:
		os.system('shutdown -s')
	else:
		print 'Pardon, sir'

# daemon always on
def daemon():

	text = voice.listen()

	if text == None:
		return
	if text[:6] == 'alfred':	# wake up Alfred
		alfred()

if __name__ == '__main__':

	while(True):
		daemon()