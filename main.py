# Text version
# i.e. Python says what you write
import pyttsx3

friend = pyttsx3.init()

# Speaking Rate
rate = friend.getProperty('rate')
print(rate)
# change_rate
cr = input('Enter rate:')
friend.setProperty('rate', cr)

# Voice
voice = friend.getProperty('voices')
# change_voice_here
friend.setProperty('voice', voice[0].id)

while True:
    print('')
    speech = input('Hello, Please type what you want to hear')
    friend.say(speech)
    friend.runAndWait()
