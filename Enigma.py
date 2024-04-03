import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
from PIL import Image
import psutil
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    
    engine.runAndWait()

#speak('My name is Enigma, I am a prototype created by Zion to help strengthen human existence, please enter password to continue')


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the currrent time is")
    speak(Time)

#time()



def date():
    speak("the current date is")
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
#date()
    

def wishme():
    speak("welcome back sir")
    #speak("the currrent time is")
    time()
    #speak("the current date is")
    date()
    hour = datetime.datetime.now().hour
    if hour  >= 6 and hour <12:
        speak("good morning sir!")
    elif hour >=12 and hour <18:
        speak("good afternoon sir!")
    elif hour >=18 and hour <24:
        speak("good evening sir!")
    else:
        speak("good night sir!")

    speak("Enigma at your service please tell me how I can help you")

#wishme()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listen...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("say that again...")
        return "None"
    return query

#takecommand()

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("alexmorganwaves@gmail.com","Amazon1@")
    server.sendmail("omezirizion@gmail.com",to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save('ss.png ')

def cpu():
    usage= str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery= psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())






if __name__ =="__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("what should I say...")
                content = takecommand()
                to = 'omezirizion@gmail.com'
                sendemail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("unable to send email")

        elif 'search in chrome' in query:
            speak('what should I search')
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        
        elif "log out" in query:
            os.system("shutdown -1")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play song" in query:
            songs_dir = "C:/Users/DEV ZION/Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif "remember that" in query:
            speak("what should I remember")
            data = takecommand()
            speak("You said I should remember" + data)
            remember  = open('data.txt','w')
            remember.write(data) 
            remember.close() 
        elif  "do you know anything" in query:
            remember = open('data.txt', 'r')
            speak("You said I shoul remember that" +remember.read())  
        
        elif "take a screenshot" in query:
            screenshot()
            speak('Done!')

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()

        elif 'offline' in query:
            speak("Going offline...")
            quit()