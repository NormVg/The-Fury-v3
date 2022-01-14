import datetime
from speak import speak
import random
from datetime import date
import os
from PyDictionary import PyDictionary as diction
from time import sleep
from listen import take_command
from keyboard import write
import requests,json
import calendar
def tell_time():###################
    time = datetime.datetime.now().strftime('%I:%M:%S %p')
    print(time)
    rn = f"time is {time}",f"boss the time is {time}",f"{time}"
    rn = random.choice(rn) 
    speak(rn)
def date_tomm():####################
    presentday = datetime.datetime.now()
    tommor = presentday + datetime.timedelta(1)
    weak = calendar.day_name[tommor.weekday()]
    speak(f"its {weak}")
    speak(tommor.strftime('%d-%m-%Y'))


def date_yester():########################
    presentday = datetime.datetime.now()
    tommor = presentday - datetime.timedelta(1)
    weak = calendar.day_name[tommor.weekday()]
    speak(f"its {weak}")
    speak(tommor.strftime('%d-%m-%Y'))    


def tell_date():#########################
    today = date.today()
    weak = calendar.day_name[today.weekday()]
    speak(f"its {weak}")
    print("Boss Today's date:", str(today))
    speak("boss today date is" + str(today))

def movie():########################
     movie_dir = "C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\movie\\"
     movies = os.listdir(movie_dir)
     rd = random.choice(movies) 
     os.startfile(os.path.join(movie_dir, rd))
     speak("i think you might like this boss") 
     

            
def music():###############################
    music_dir = "C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\music\\"
    songs = os.listdir(music_dir)
    rd = random.choice(songs) 
    os.startfile(os.path.join(music_dir, rd))
    speak("playing.. music boss,,")

def mean(command):#######################
    command = str(command)
    try:
         command = command.replace("tell the meaning of ","")
         result = diction.meaning(command)
         speak(f"the meaning of {command} is {result}")
    except:
         command = command.replace("tell the meaning of ","")
         speak('can not get the meaning of ' + command)




def countdown10():####################
                speak("starting countdown")
                speak("ten")
                sleep(1)
                speak("nine")
                sleep(1)
                speak("eight")
                sleep(1)
                speak("seven")
                sleep(1)
                speak("six")
                sleep(1)
                speak("five")
                sleep(1)
                speak("four")
                sleep(1)
                speak("three")
                sleep(1)
                speak("two")
                sleep(1)
                speak("one")
                speak("zero")
                speak("go, go, go")

def note_maker():########################
            os.startfile("C:\\Users\\Arun Gupta\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk")
            sleep(1.5)
            speak("speak boss i am noting it down")            
            text = take_command()
            text = str(text)
            write(text)

def count_three():###################3
    sleep(1)
    speak("one")
    sleep(1)
    speak("two")
    sleep(1)
    speak("three")
    
def joke():####################
    joke = requests.get("https://indian-jokes-api.herokuapp.com/jokes/random")
    jokes = joke.content
    j= json.loads(jokes)
    ops = j["text"]
    print(ops)

def coin_toss():#####################
            speak('ok, on count of three')
            count_three()
            result = ("head","tale")
            tr = random.choice(result)
            speak("tossed result is" + tr)
            print(tr)

def speak_for_me():####################
             speak("what should i speak boss")
             spek = take_command()
             speak(spek) 

