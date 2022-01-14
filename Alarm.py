from plyer import notification
from playsound import playsound
import datetime
import pyttsx3

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def notify(topic,dec):

    
    playsound("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\python fury assistant project\\Extra\\notification.mp3")              
    notification.notify(
        title = topic,
        message = dec,
        app_icon = "C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\ICO.ico",
        timeout = 10
    )

def RingerNow():
    extracted_time = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\alarm.txt",'rt')
    time = extracted_time.read()
    Time = str(time)


    while True:

        current_time = datetime.datetime.now().strftime("%H:%M")
        print(current_time)
        if current_time == Time:
            notify("alarm",f"this is an alarm of time {Time}")
            speak("boss i am sorry to disturb but it is an alarm for you")
            delete_time = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\alarm.txt",'r+')
            delete_time.truncate(0)
            delete_time.close()
        elif current_time>Time:
            break
RingerNow()

