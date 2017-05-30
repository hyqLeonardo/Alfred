import speech_recognition as sr

# audio to text
def listen():
	# obtain audio from the microphone
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Now I'm listening ~")
		audio = r.listen(source)

	# recognize speech using Microsoft Bing Voice Recognition
	BING_KEY = "72c9268836d5478980d267984273358a"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
	try:
		text = r.recognize_bing(audio, key=BING_KEY)
		print text
		return text
	except sr.UnknownValueError:
		print("I could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from the service; {0}".format(e))

	# # recognize speech using Sphinx
	# try:
	#     text = r.recognize_sphinx(audio)
	#     print("I thinks you said " + text)
	#     serve(text)
	# except sr.UnknownValueError:
	#     print("I could not understand audio")
	# except sr.RequestError as e:
	#     print("Error; {0}".format(e))
