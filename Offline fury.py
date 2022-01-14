from keyboard import press_and_release
from time import sleep
from pyautogui import click
from pyautogui import press
import datetime
import random
from datetime import date
import os
from keyboard import write
import calendar
import pyttsx3

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

import pyautogui
from keyboard import press_and_release
from keyboard import write
from time import sleep
from keyboard import press
from keyboard_input import take_querry
from pyautogui import leftClick
import os
import random



def take_querry():
    command_k = input("command : ")

    return command_k



def shotcut(command):
        if "volume up" in command:
                 pyautogui.press("volumeup")
                 pyautogui.press("volumeup")
                 pyautogui.press("volumeup")
                 pyautogui.press("volumeup")
                 pyautogui.press("volumeup")
        elif "volume down" in command:
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
        elif "mute" in command:
                pyautogui.press("volumemute")        
        elif 'pause' in command:
                pyautogui.press('space bar')
        elif "skip" in command:
                pyautogui.press('i')
        elif "full screen" in command:
                pyautogui.press("f")
        elif "lock system" in command:
                press_and_release('windows + l')
        elif 'resume' in command:
                press('space bar')
        elif 'back' in command:
                press('j')
        elif 'previous video' in command:
                press_and_release('SHIFT + p')
        elif 'next video' in command:
                press_and_release('SHIFT + n')
        elif 'new tab' in command:
                press_and_release('ctrl + t')
        elif 'close tab' in command:                                                                                                                                                                                        
                press_and_release('ctrl + w')
        elif 'new window' in command:
                press_and_release('ctrl + n')
        elif 'show history' in command:
                press_and_release('ctrl + h')
        elif 'show download' in command:
                press_and_release('ctrl + j')
        elif 'private window' in command:
                press_and_release('Ctrl + Shift + n')
        elif "task manager" in command:
                press_and_release('ctrl + shift +esc') 
        elif "zoom in" in command:
                press_and_release('windows + =')
                sleep(1)
                press_and_release('windows + =')
        elif "zoom out" in command:
                press_and_release('windows + -')
                sleep(0.2)
                press_and_release('windows + -')
        elif "exit zoom" in command:
                press_and_release('windows + esc')
                sleep(0.2)
                press_and_release('windows + esc')
        elif "create folder" in command:
                opt = 'give the name of the folder name','folder name','name of the folder','name the folder'
                opr = random.choice(opt)
                speak(opr)
                name = take_querry()
                sleep(5)
                press_and_release('ctrl + shift + n')
                sleep(0.5)
                name = str(name)
                write(name)
                leftClick()
        elif "show drive" in command:
                press_and_release('windows + e')
        elif "select all" in command:
                press_and_release("ctrl + a")
        elif "copy"  in command:
                press_and_release("ctrl + c")
        elif "paste" in command:
                press_and_release("ctrl + v")
        elif 'home screen' in command:
                press_and_release('windows + m')
        elif 'minimize' in command:
                press_and_release('windows + m')
        elif 'show start' in command:
                press('windows')
        elif 'open setting' in command:
                press_and_release('windows + i')
        elif 'open search' in command:
                press_and_release('windows + s')
        elif "switch window" in command:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.keyUp("alt")
        elif "take screenshot" in command:
                speak("boss, please what name should i give to screenshot")
                name = take_querry().lower()
                speak("please hold on i am taking screenshot")
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("screenshot has been taken boss")
        elif "show photo" in command:
             os.startfile("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\Photos.lnk")
        elif "get me new desktop" in command:
                pyautogui.hotkey('winleft','ctrl','d')
        else:
                speak("sorry")


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
            text = take_querry()
            text = str(text)
            write(text)

def count_three():###################3
    sleep(1)
    speak("one")
    sleep(1)
    speak("two")
    sleep(1)
    speak("three")
    

def coin_toss():#####################
            speak('ok, on count of three')
            count_three()
            result = ("head","tale")
            tr = random.choice(result)
            speak("tossed result is" + tr)
            print(tr)

def speak_for_me():####################
             speak("what should i speak boss")
             spek = take_querry()
             speak(spek) 
def app_opener(command):
    open = command.replace('open',"")##############
    speak(f'opening {open} boss')     
    press_and_release("windows + s")
    sleep(1)
    click(x=150, y=706)
    write(open)
    sleep(1)
    press("enter")

def windowsSearch(command):################################
    if "app" in command:
        command = str(command)
        command = command.replace("open","")
        command = command.replace('app','')
        press_and_release('windows + s')
        sleep(.7)
        click(x=150, y=706)
        write(f"apps: {command}")
        sleep(1)
        press("enter")
    
    elif 'hit' in command:
        command = str(command)
        command = command.replace('hit','')
        press_and_release('windows + s')
        sleep(.7)
        click(x=150, y=706)
        write(f"music: {command}")
        sleep(1)
        press("enter")
    elif 'film' in command:
        command = str(command)
        command = command.replace('film','')
        command = command.replace('play','')
        press_and_release('windows + s')
        sleep(.7)
        click(x=150, y=706)
        write(f"video: {command}")
        sleep(1)
        press("enter")

def lastTimeSaver():
    today = datetime.datetime.now().strftime('%d-%m')
    Time_input = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\after a long time.txt","a")
    Time_input.write(today)
    Time_input.close()

def lastTimedelete():
    delete_time = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\after a long time.txt",'r+')
    delete_time.truncate(0)
    delete_time.close()
#extracting date
extracted_time = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\after a long time.txt",'rt')
time = extracted_time.read()
Time = str(time)
def last_time():
    #today = datetime.datetime.now().strftime('%d-%m')
    datetoday = datetime.datetime.now().strftime('%d')
    monthtoday = datetime.datetime.now().strftime('%m')

    
    DM = Time.split('-', maxsplit=1)
    lastdate = DM[0]
    lastmonth = DM[1]

    ########################################

    lastdate = int(lastdate)
    lastmonth = int(lastmonth)
    datetoday = int(datetoday)
    monthtoday = int(monthtoday)
    #datetoday = int('1')

    ###############################################

    if (datetoday - lastdate) >= 2 or (lastdate - datetoday) >= 2 and (monthtoday == lastmonth):
        speak("it is good to see you after a long time boss")
    
    elif (datetoday - lastdate) == 1 and (monthtoday == lastmonth):
        speak('nice to meet you again')
    
    elif (datetoday == lastdate) and (monthtoday == lastmonth):
        speak('hello again boss')

    elif (31 == lastdate) or (30 == lastdate) and (datetoday == 1):
        speak('nice to meet you again')

    else:
        speak('love to meet you again')

    lastTimedelete()
    sleep(1)
    lastTimeSaver()



import pandas 
import datetime

import time

def ocation():
    df = pandas.read_excel("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\Ocation.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")
    year = datetime.datetime.now().strftime("%Y")

    for index, item  in df.iterrows():

        oday = item['date'].strftime("%d-%m")
     #   print(oday)
        #oday = int(oday)
        
       # print(df)
        if  (today == oday):
            ocation = item['ocation']
            diloge = item['diloge']
            speak(f"boss today is {ocation}")
            
            time.sleep(.5)
            speak(diloge)
        else:
            pass

def ocationReminder():
    df = pandas.read_excel("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\Ocation.xlsx")
    #tomorow = datetime.datetime.now()
    presentday = datetime.datetime.now()
    tommor = presentday + datetime.timedelta(1)
    tommor = tommor.strftime("%d-%m")
    year = datetime.datetime.now().strftime("%Y")

    for index, item  in df.iterrows():

        oday = item['date'].strftime("%d-%m")

        if  (tommor == oday):
            ocation = item['ocation']
            #diloge = item['diloge']
            speak(f'boss tomorrow is {ocation}')
        else:
            pass

def wish():
    hour1 = datetime.datetime.now().hour
    hour = int(hour1)
    
    if hour>=0 and hour<=12:
        rr = 'good morning','morning boss','good morning boss','how is your morning boss'
        re = random.choice(rr)
        speak(re)
    elif hour>12 and hour<17:
        rr = 'good afternoon boss','afternoon boss', 'its afternoon'
        re = random.choice(rr)
        speak(re)
    elif hour>17 and hour<20:
        rr = 'good evening boss','evening boss','its snack time'
        re = random.choice(rr)
        speak(re)
    elif hour>20:
        rr = "its night boss",'i think you should sleep','its late night you should take rest'
        re = random.choice(rr)
        speak(re)
    
    last_time()
    speak('i am your assistant')
    rr = 'is there something i could help','how may i help you boss','how may i help you','may i do something for you'
    re = random.choice(rr)
    speak(re)
    ocation()
    ocationReminder()
    

def exe(Command):
    command = str(Command)
    
    if 'time' in command:
        tell_time()
    elif 'tomorrow date' in command:
        date_tomm()
    elif 'yesterday date' in command:
        date_yester()
    elif 'date' in command:
            tell_date()
    elif 'open' in command:
            app = str(command)
            app = app.replace('open ','')
            app_opener(app)
    elif "film" in command:
        windowsSearch(command)
    elif "hit" in command:
        windowsSearch(command)
    elif "app" in command:
        windowsSearch(command)
    elif 'play some movie' in command:      
            movie()
    elif 'play some music' in command:
        music()
    elif 'countdown' in command:
        countdown10()
    elif 'on count of three' in command:
        count_three()
    elif 'make a note' in command:
        note_maker()
    elif 'toss a coin' in command:
        coin_toss()
    elif 'speak for me' in command:
        speak_for_me()
    elif 'wait' in command:
        try:
            wait = command.replace('wait ','')
            wait = wait.replace(' second','')
            speak(f'wating for {wait} second')
            wait = int(wait)
            sleep(wait)
        except:
            speak('sorry boss')
    elif "close" in command:
             try:

                close = command.replace("close","")
                speak(f"closing {close}")
                os.system(f"taskkill /f /im {close}")
             except:
                 close = command.replace("close","")
                 speak('can not close ' + close + 'please do it manualy')

    elif "show program files" in command:
             speak("opening")
             os.startfile("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury")
    elif"exit my files " in command:
             speak("closing Vishnu Gupta's File")
             os.system("taskkill /f /im Vishnu Gupta's File")
    elif "show my file" in command:
             npath = "C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File"
             os.startfile(npath)
    
    elif "send email" in command:
        speak("not avalable in offline mode")
    elif "remind" in command and "later" in command:
        speak("what i have to remind")
        remind = take_querry()
        command_input = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\reminder.txt","a")
        command_input.write(remind)
        command_input.close()
    elif ("remind" in command) and ("me" in command) and ("said" in command) or ("i am forgeting something" in command):
        speak("sir you said me to remind")
        extracted_time = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\reminder.txt",'rt')
        time = extracted_time.read()
        command = str(time)
        command = command.replace('me' , "you")
        commandop = command.replace("you" , "me")
        speak(commandop)
        delete_time = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\reminder.txt",'r+')
        delete_time.truncate(0)
        delete_time.close()

            
    else: 
        shotcut(command)#chatbot is inside this










def run_offline_fury():
    
    while True:
        query = take_querry()
        query = str(query)
        try:
            if 'and' in query:
                SPLIT = query.split(' and ',maxsplit=1)
                command = SPLIT[0]
                command2 = SPLIT[1]
                command = command.lower()
                command2 = command2.lower()
                print(command)
                print(command2)
                exe(command)
                if "sleep" in command2:
                    speak("you can call me anytime boss")
                    lastTimedelete()
                    sleep(.5)
                    lastTimeSaver()
                    break
                else:
                    exe(command2)
            if "or" in query:
                    SPLITOR = query.split(" or ", maxsplit=1)
                    print(SPLITOR)
                    command = random.choice(SPLITOR)
                    speak(f"i would like to {command}")
                    print(command)
                    exe(command)
            else:
                print(query)
                if "sleep" in query:
                    speak("you can call me anytime boss")
                    lastTimedelete()
                    sleep(.5)
                    lastTimeSaver()
                    break
                else:
                    exe(query)
        except:
            speak('sorry what you said')
