from cvzone.SerialModule import SerialObject
import speech_recognition as sr  # pip install speechRecognition
import pyttsx3 # pip install pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

try:
    arduino = SerialObject('COM5')
except:
    print("<<<-------------------!!Bulb Not Connected!!------------------>>>")

def speak(audio):
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait() 

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(": Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f": User said : {query}\n")
    except:
        # print(e)
        print(": Say that again please...")
        return "None"
    return query

while True:
  
  query = takeCommand().lower()

  
  if 'bulb on' in query:
                arduino.sendData([1,0])
                speak("Bulb on Sir.")

  elif 'bulb off' in query:
                arduino.sendData([0,0])
                speak("Bulb off Sir.")
