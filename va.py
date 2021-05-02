import speech_recognition as sr #import impoortant lybrary
from time import ctime
import time
import os
from gtts import gTTS
import requests, json


def listen():  #This uses the SpeechRecognition library to activate your machine’s microphone, and then converts the audio to text in the form of a string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data
    
    
def respond(audioString): #This uses the gTTS library take a string input, prints it then convert the string to an audio file.  This audio file is saved to the local directory and then played by our operating system.

    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")
    
    
def digital_assistant(data):  #Voiced Responses
    if "how are you" in data:
        listening = True
        respond("I am well")
    if "what time is it" in data:
        listening = True
        respond(ctime())
        
    if "stop listening" in data:
        listening = False
        print('Listening stopped')
        return listening
    return listening
    
time.sleep(2)
respond("Hi Dante, what can I do for you?")
listening = True
while listening == True:
    data = listen()
    listening = digital_assistant(data)
    
    
#Google Maps Query
def digital_assistant(data):
    if "how are you" in data:
        listening = True
        respond("I am well")
    if "what time is it" in data:
        listening = True
        respond(ctime())
    if "where is" in data:
        listening = True
        data = data.split(" ")
        location_url = "https://www.google.com/maps/place/" + str(data[2])
        respond("Hold on Dante, I will show you where " + data[2] + " is.")
        maps_arg = '/usr/bin/open -a "/Applications/Google Chrome.app" ' + location_url
        os.system(maps_arg)
        
    if "stop listening" in data:
        listening = False
        print('Listening stopped')
        return listening
    return listening
    
    #Weather Query
    def digital_assistant(data):
    global listening
    if "how are you" in data:
        listening = True
        respond("I am well")
    if "what time is it" in data:
        listening = True
        respond(ctime())
    if "where is" in data:
        listening = True
        data = data.split(" ")
        location_url = "https://www.google.com/maps/place/" + str(data[2])
        respond("Hold on Dante, I will show you where " + data[2] + " is.")
        maps_arg = '/usr/bin/open -a "/Applications/Google Chrome.app" ' + location_url
        os.system(maps_arg)
     if "what is the weather in" in data:
        listening = True
        api_key = "Your_API_key"
        weather_url = "http://api.openweathermap.org/data/2.5/weather?"
        data = data.split(" ")
        location = str(data[5])
        url = weather_url + "appid=" + api_key + "&q=" + location 
        js = requests.get(url).json() 
        if js["cod"] != "404": 
            weather = js["main"] 
            temp = weather["temp"] 
            hum = weather["humidity"] 
            desc = js["weather"][0]["description"]
            resp_string = " The temperature in Kelvin is " + str(temp) + " The humidity is " + str(hum) + " and The weather description is "+ str(desc)
            respond(resp_string)
        else: 
            respond("City Not Found")
    if "stop listening" in data:
        listening = False
        print('Listening stopped')
    return listening
time.sleep(2)
respond("Hi Dante, what can I do for you?")
listening = True
while listening == True:
    data = listen()
    listening = digital_assistant(data)
    
