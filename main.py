import pyttsx3 # pip install pyttsx3
import pywhatkit  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import webbrowser
from keyboard import press, press_and_release, write #pip install keyboard
import os
import time
import wolframalpha # pip install wolframalpha
import wikipedia as googlescrap # pip install wikipedia
import sys
from pyautogui import press #pip install pyautogui
from Appcontrol import openappweb, closeappweb
import sys
from Nasa import MarsImage, NasaNews
from DataBase.Chatbot.ChatBot import ChatterBot
from Automations import Notepad, GoogleMaps, what, sendEmail
from DataBase.Features.Features import pdf_reader, battery, DateConverter, Jokes, alarm, CoronaVirus, My_Location, google_photos, show_me_some_tech_news, show_me_some_tech_videos
from pyfirmata import Arduino, SERVO
from cvzone.SerialModule import SerialObject


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

def wishMe(): 
    h = ChatterBot('wake')
    speak(h)
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:

        speak(f"its {tt}")

    elif hour >= 12 and hour <= 18:

        speak(f"its {tt}")

    else:

        speak(f"its {tt}")

def Date():
    date = datetime.datetime.now().strftime("%B %d,%y")
    speak(f"The Current Date is {date}")

def Wolfram(query):
    api_key ="A2LE58-TH54TEJ3AJ"
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)


    try:
        Answer = next(requested.results).text

        return Answer

    except:
        speak("I am sorry sir I cannot Answer this Question")

def Calculator(query):
    Term = str(query)

    Term = Term.replace("jarvis what is","")
    Term = Term.replace("multiplied by ","*")
    Term = Term.replace("plus ","+" )
    Term = Term.replace("minus ","-")
    Term = Term.replace("dived by","/")
    Term = Term.replace("calculate ","")

    Final = str(Term)
    try:
        result = Wolfram(Final)
        speak(f"The answer of this question is {result}")
    except:
        speak("I am sorry sir i cannot Answer this Question")

def Temp(query):
    
    speak("Extracting Temprature Outside...")

    temp = str(query)
    temp = temp.replace("jarvis ","")
    temp = temp.replace("in ","")
    temp = temp.replace("what is the ","")
    temp = temp.replace("temprature","")

    temp_query = str(temp)
    if 'outside' in temp_query:
        var1 = "Temprature in Lucknow"  
        Ans = Wolfram(var1)
        speak(f"{var1} is {Ans}")

    else:
        var2 = "in" + temp_query
        answ = Wolfram(var2)
        speak(f"{var2} is {answ}")

def TaskExe():
        wishMe()
        Temp('what is the temprature outside')
        while True:

            query = takeCommand().lower()
        
            # Logic for executing tasks based on query
            if 'my location' in query:
                My_Location()

            elif 'where is' in query:
                Place = query.replace("where is", "")
                Place = Place.replace("jarvis","")
                Place = Place.replace("tell me","")
                GoogleMaps(Place)

            elif 'pause' in query:

                press('space bar')

            elif 'play' in query:

                press('space bar')

            elif 'full screen' in query:

                press('f')

            elif 'film screen' in query:

                press('t')

            elif 'forward' in query:

                press('l')

            elif 'back' in query:

                press('j')

            elif 'previous' in query:
                

                press_and_release('SHIFT + p')

            elif 'next' in query:

                press_and_release('SHIFT + n')
        
            elif 'mute' in query:

                press('m')

            elif 'unmute' in query:

                press('m')

            elif 'my channel' in query:

                webbrowser.open("https://www.youtube.com/channel/UClCR78mI9CMLsnDcJzUVGVg")

            elif 'home screen' in query:

                press_and_release('windows + m')

            elif 'show start' in query:

                press('windows')
                speak("As You Wish Sir")

            elif 'open setting' in query:

                press_and_release('windows + i')
                speak("Opening settings sir")

            elif 'open search' in query:

                press_and_release('windows + s')
                speak("opening search bar sir")

            elif 'restore windows' in  query:

                press_and_release('Windows + Shift + M')
                speak("Restoring windows Sir!")

            elif 'switch to application' in query:
                app = query.replace("switch to application","")
                

                try:
                    press(f'Windows + {app}')
                    speak(f"opening application {app} sir!")

                except:
                    speak("cannot do this task for now sir!")

            elif 'new tab' in query:

                press_and_release('ctrl + t')
                speak("Opening new tab")

            elif 'close tab' in query:

                press_and_release('ctrl + w')
                speak("Closing Tab sir")

            elif 'new window' in query:

                press_and_release('ctrl + n')
                speak("Opening New Window sir")

            elif 'history' in query:

                press_and_release('ctrl + h')
                speak("Opening Your History sir")

            elif 'download' in query:

                press_and_release('ctrl + j')
                speak("Here are Your Downloads Sir")

            elif 'bookmark' in query:

                press_and_release('ctrl + d')
                speak("Book Marking This Page sir")

                press('enter')

            elif 'incognito' in query:

                press_and_release('Ctrl + Shift + n')
                speak("Opening New Icognito Tab Sir")

            elif 'switch tab' in query:

                tab = query.replace("switch tab ", "")
                Tab = tab.replace("switch tab","")
            
                num = Tab

                try:
                    bb = f'ctrl + {num}'

                    press_and_release(bb)
                    speak("Switching the tab sir")

                except:
                    speak("try again, an error occured")

            elif 'are you there' in query:
                speak('YES Sir!')
                print()

            elif 'open youtube' in query:
                webbrowser.open("www.youtube.com")
                speak('Opening YouTube')

            elif 'open google' in query:
                webbrowser.open("www.google.com")
                speak('Opening Google')

            elif 'open stackoverflow' in query:
                webbrowser.open("www.stackoverflow.com")
                speak('Opening StackoverFlow')

            elif 'music' in query:
                music_dir = 'E:\\Jarvis EXE\\DataBase\\FavroitesMusics\\Favroites'
                songs = os.listdir(music_dir)
                speak("Playing Your Favroites Sir!")
                os.startfile(os.path.join(music_dir, songs[0]))
 
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                codePath = "C:\\Users\\csp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                speak("Opening Code!")
                os.startfile(codePath)

            elif 'email to my father' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "snavinekma@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend Krishna bhai. I am not able to send this email")

            elif 'corona' in query:

                speak("Which Country's information you want sir")
                content = takeCommand()

                CoronaVirus(content)

            elif 'whatsapp message' in query:
                name = query.replace("whatsapp message","")
                name = name.replace("send ","")
                name = name.replace("send ","")
                name = name.replace("to","")
                Name = str(name)
                speak(f"Whats the message for {Name}")
                MSG = takeCommand()
                what(Name, MSG)

            elif 'temperature' in query:
                Temp(query)
 
            elif 'increase volume' in query:
                press("volumeup")

            elif 'joke' in query:
                Jokes()

            elif 'search' in query:
                query = query.replace("jarvis","")
                query = query.replace("search","")
                query = query.replace("on","")
                query = query.replace("google","")
                query = query.replace("for","")
                speak("This is what I Found, Related to your Query Sir!")
                pywhatkit.search(query)
                try:

                    result = googlescrap.summary(query,2)
                    speak(result)

                except:
                    speak("Cannot find speakable Data sir!")
             
            elif 'read' in query:
                pdf_reader()

            elif 'battery' in query:
                speak("Extracting battery info sir!")
                battery()

            elif "open" in query:
                openappweb(query)
            
            elif "close" in query:
                closeappweb(query)
            
            elif 'remember that' in query:
                rMsg = query.replace("remember that","")
                rMsg = rMsg.replace("jarvis","")
                speak("Ok sir! You Told me to Remind you that :"+rMsg)
                remember = open('JarvisRememberFile.txt','w')
                remember.write(rMsg)
                remember.close()

            elif 'what do you remember' in query:
                remember = open('JarvisRememberFile.txt','r')
                speak("You told me that : "+remember.read())

            elif 'space news' in query:
                try:
                    speak("Tell me the Date for News Extraction Process .")
                    Date = takeCommand()
                    Value = DateConverter(Date)
                    NasaNews(Value)
                except:
                    speak("News Extraction Failed")

            elif 'Mars image' in query:
                MarsImage()

            elif 'change Friday' in query:
                engine.setProperty('voice', voices[2].id)
                speak("Voice changed")

            elif 'volume down' in query:
                speak("Initializing Volume down....")
                press("volumedown")
                speak("Done Sir!")

            elif 'volume up' in query:
                speak("Initializing Volume Up....")
                press('volumeup')
                speak("Done Sir!")

            elif 'break' in query:
                speak("")
                break

            elif 'write a note' in query:
                Notepad()

            elif "set alarm" in query:
                print("input time example:- 10 and 10 and 10")
                speak("Set the time")
                a = input("Please tell the time :- ")
                alarm(a)
                speak("Done,sir")

            elif 'terminate' in query:
                speak("Ok Sir Just Say Wake Up Jarvis")
                sys.exit()
            
            elif 'shutdown' in query:
                speak("Ok Sir Just Say Wake Up Jarvis")
                sys.exit()
                    
            elif 'rest' in query:
                speak("Ok Sir Just Say Wake Up Jarvis")
                break

            elif 'exit' in query:
                    speak("Ok Sir Just Say Wake Up Jarvis")
                    break

            elif 'try on YouTube' in query:
                v = query.replace("try on YouTube","")
                v = v.replace("jarvis","")

                webbrowser.open(f"https://www.youtube.com/results?search_query={v}")
                speak("Done sir")

            elif 'bulb on' in query:
                arduino.sendData([1,0])
                speak("Bulb on Sir.")

            elif 'bulb off' in query:
                arduino.sendData([0,0])
                speak("Bulb off Sir.")

if __name__ == "__main__":
    TaskExe()

    while True:

        query = takeCommand().lower()
        
        if 'shutdown' in query:
            speak("As You Wish Sir , Exiting the Program...")
            sys.exit()

        elif 'terminate' in query:
            speak("As You Wish Sir , Exiting the Program...")
            sys.exit()
        
        elif 'exit' in query:
            speak("As You Wish Sir , Exiting the Program...")
            sys.exit()

        elif 'wake' in query:
            TaskExe()

        elif 'jarvis' in query:
            TaskExe()

        elif 'back' in query:
            TaskExe()

        elif 'i am back' in query:
            TaskExe()

