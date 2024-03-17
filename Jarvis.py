import os
from typing import Any
from PyQt5.QtWidgets import QWidget
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import psutil
import pywhatkit
import pyautogui
import pyjokes
import requests
import bs4 as BeautifulSoup
import requests
import json
from win32com.client import Dispatch
import webbrowser
import sys
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarbot import Ui_MainWindow




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning SIR")
        speak("Good Morning SIR")
    elif hour >= 12 and hour < 17:
        print("Good Afternoon SIR")
        speak("Good Afternoon SIR")
    elif hour >= 17 and hour <21:
        print("Good Evening SIR")
        speak("Good Evening SIR")
    else:
        print("Good Night SIR")
        speak("Good Night SIR")

    speak("i am jarvis sir, please tell me how can i help you ?")

def alarm(query):
    timehere = open("alarm.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def news():
    main_url="https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=bdde1747019347d199bc69cb16faa199"
    main_page=requests.get(main_url).json()
    articles = main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")






class MainThread(QThread):
    def __init__(self, speak_function):
        super(MainThread, self).__init__()
        self.speak = speak_function

    def run(self):
        self.TaskExecution()



    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            print("wait for few moments...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You just said: {query}\n")
        except Exception as e:
            print(e)
            speak("Please Tell me again")
            query ="none"
        return query


    def TaskExecution(self):
        wish()
        while True:
        
                
            self.query = self.takecommand().lower()
                    
            if 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime) 
                self.speak(f"Sir, the time is {strTime}")


            elif "open google" in self.query:
                self.speak("sure sir")
                self.speak("sir, what should i search on gooogle ?")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")

            elif "what can you do for me" in self.query:
                self.speak("Nice question! sir")  
                self.speak("As per my program, I\'m a bot which can perform task through your voice commands.")
                    
            elif "cool" in self.query or "nice" in self.query or "awesome" in self.query or "thank you " in self.query:
                self.speak("Yes sir, Thats my pleasure!")

            elif "name" in self.query:
                self.speak("My name is Jarvis")

            elif "created" in self.query:
                self.speak("master gaurav has created me. he is my god")
                        


            elif 'wikipedia' in self.query:
                self.speak("searching in Wikipedia...")
                try:
                    self.query = self.query.replace("wikipedia", "") 
                    results = wikipedia.summary(self.query, sentences=1)
                    self.speak("According to wikipedia,")
                    print(results)
                    self.speak(results)
                except:
                    self.speak("no results found")
                    print("No results found")
            
            elif 'play' in self.query:
                self.query = self.query.replace("play", "")
                self.speak('Playing ' + self.query) 
                pywhatkit.playonyt(self.query)

            elif 'type' in self.query:
                self.speak("Please tell me what should i write")
                os.startfile("C:\\Windows\\notepad.exe")
                while True:
                    writeInNotepad = self.takecommand()
                    if writeInNotepad=='exit typing':
                        self.speak("Done Boss")
                    else:
                        pyautogui.write(writeInNotepad) 
                    break 

            elif 'joke' in self.query:
                joke =pyjokes.get_joke()
                print(joke)
                self.speak(joke)

            elif "how much power left" in self.query or "how much power we have" in self.query or "battery" in self.query:
                battery =psutil.sensors_battery()
                percentage= battery.percent
                self.speak(f"sir our system has {percentage} percent battery")
                if percentage >=75:
                    self.speak("sir, we have enough battery to continue the work")
                elif percentage>=40 and percentage<=75:
                    self.speak("sir, we should connnect our system to charging point to charge our battery")
                elif percentage<=15 and percentage<=30:
                    self.speak("sir, we dont have enough power to work, please connect to charging")
                elif percentage<=15:
                    self.speak("sir, we have very low power, system can shutdown anytimer")
        

            elif "mute" in self.query:
                self.speak("I'm muting Sir...")
                break

            elif 'exit program' in self.query:
                self.speak("I am leaving sir, good bye and have a nice day!")
                sys.exit()

            elif 'close the window' in self.query or 'close the application' in self.query:
                self.speak("closing the application sir...")
                pyautogui.hotkey('ctrl','w')

            elif 'screenshot' in self.query:
                self.speak("Taking screenshot...")
                pyautogui.press('prtsc')
                    
            elif 'minimize' in self.query or 'minimise' in self.query:
                self.speak("Minimizing...")
                pyautogui.hotkey('win','down','down')

            elif 'maximize' in self.query or 'maximise' in self.query:
                self.speak("Maximizing...")
                pyautogui.hotkey('win','up','up')

            elif 'song' in self.query or 'sing a song' in self.query or 'getting bored' in self.query:
                self.speak("ok sir , let me play something for you !")
                self.speak("Please wait a moment...")
                songs = os.listdir('H:\MUSIC')
                os.startfile(os.path.join('H:\MUSIC',songs[0]))  
            elif 'pause' in self.query or 'pass' in self.query:
                pyautogui.press('space')
                self.speak("Done sir")

            elif "open facebook" in self.query:
                self.speak("Opening facebook sir...")
                webbrowser.open('http://www.facebook.com')


            elif "open youtube" in self.query:
                self.speak("Opening youtube sir...")
                
                webbrowser.open('http://www.youtube.com')

            

            elif "set alarm" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("please input the time sir , for example, 4 and 10 and 30")
                    print("Listening...")
                    r.pause_threshold = 1
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source)
                a=r.recognize_google(audio)
                self.speak("Set the time")
                alarm(a)
                self.speak("Done boss") 


            elif "thank you" in self.query:
                self.speak("your welcome sir")

            elif "more about yourself" in self.query:
                self.speak("sure sir! my name is jarvis and i am a virtual robot that can perform task through your voice commands. i was created by gaurav sir. i can perfom many tasks like playing music, opening the applications, respond to your queries, writing in notepad, setting aalarm and many more like that.")

            

            elif "weather" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("sir tell me the name of the city please !")
                    print("Listening...")
                    r.pause_threshold = 1
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source)
                my_str=r.recognize_google(audio)

                self.speak(my_str)
                url=f"https://api.weatherapi.com/v1/current.json?key=201ef23aa6534f92a4770105232409&q={my_str}"
                r = requests.get(url)
                self.speak = Dispatch("SAPI.SpVoice").speak
                wdic=json.loads(r.text)  
                a=(wdic["current"]["temp_c"])
                self.speak(f"The current temperature of {my_str} is {a} degrees Celsius")

            elif "shutdown system" in self.query:
                self.speak("sir , Are you sure you want to shut down my system ?")
                shutdown = input("Do you wish to shutdown your system ? (y/n): ")
                if shutdown == "y":
                    os.system("shutdown /s /t 5")
                    self.speak("Sir, I have shut down your system")

                elif shutdown == "n":
                    self.speak("Sir, I am not shutting down your system")
                    break

            elif "tell me news" in self.query:
                self.speak("please wait sir, fetching the latest news...")
                news()

            elif "restart the system" in self.query:
                self.speak("Sir, I am restarting your system")
                os.system("restart /r /t 5")   

            elif "you may sleep now" in self.query:
                self.speak("ok sir, thank u very much")
                break

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")



            elif "open" in self.query:
                self.query = self.query.replace("open", "")
                self.query = self.query.replace("jarvis", "")
                pyautogui.press("super")
                pyautogui.typewrite(self.query)
                pyautogui.sleep(2)
                pyautogui.press("enter")
                 
######################################### JARVIS 2.0 TRIOLOGY ##########################################################################################
               
        
            
#######################################################################################################################################################

startExecution = MainThread(speak)

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    
    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\\Lenovo\\Downloads\\wp2757832-wallpaper-gif.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\Lenovo\\Downloads\\Jarvis_Loading_Screen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
    
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date=QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date= current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText(label_date)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
sys.exit(app.exec_())