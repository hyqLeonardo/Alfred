# -*- coding: utf-8 -*-

import voice
import action

def alfred():

	text = voice.listen()
	print("Sir, I think you said " + text)

	if text == 'play me some music':
		action.open_web('http://music.163.com/')
	elif "search for" in text:
		action.search_web(text.replace('search for ', ''))
	else:
		print 'Pardon, sir'

# daemon always on
def daemon():

	text = voice.listen()

	if text == None:
		pass
	if text[:6] == 'alfred':	# wake up Alfred
		alfred()

if __name__ == '__main__':

	while(True):
		daemon()