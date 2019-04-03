from gtts import gTTS
from playsound import playsound
import os
import sys
language = 'en'

lst = [ 'Netherlands','Belgium','France','Germany','Danmark' ]
lst = str(lst)
myobj = gTTS(text=lst,lang = language, slow = False)
myobj.save('Test.mp3')
print("Test.mp3 file created....")
playsound("Test.mp3")
print("Test mp3 played .. Thanks")

# from command line argument 
#converting text to speech


# temp = str(sys.argv)
# print (temp)
# myobj = gTTS(text=temp,lang = language, slow = True)
# myobj.save('Test.mp3')
# print("Test.mp3 file created....")
# playsound("Test.mp3")
# print("Test mp3 played .. Thanks")


##reading from file and 
#converting the file to text


# with open('text.txt')as file:
# 	data = file.readlines()
# 	data = str(data)
# 	#print (type(data))

# 	myobj = gTTS(text=data,lang = language, slow = True)
# 	myobj.save('Test.mp3')
# 	print("Test.mp3 file created....")
# 	playsound("Test.mp3")
# 	print("Test mp3 played .. Thanks")
# 	#os.system('mpg321 Test.mp3')


	
