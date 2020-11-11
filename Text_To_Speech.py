#Instll below:
#pip install pyttsx3
#pip install pywin32

import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate

newVoiceRate = 50
#while newVoiceRate < 300:
engine.setProperty('rate', newVoiceRate)
    #engine.say('Testing different voice rates.')
    #engine.runAndWait()
    #newVoiceRate = newVoiceRate + 50
#engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 1 for female

text = input("Enter the text which you want to convert to speech: ")
engine.say(text)
engine.runAndWait()