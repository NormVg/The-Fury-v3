import pyautogui
import speech_recognition as sr
from time import sleep 
import os
from wish import wish
from  whatsapp_auto_message import WhatsappMsg
from keyboard_input import take_querry
from speak import speak
from web_and_apps import *
from basic_features import *
from shotcut_prog import shotcut
from Alarm2 import alarm
from temperature import *
from last_time import *
import basic_features
#from vosk import Model , KaldiRecognizer
#import pyaudio

from weatherAPI import weather
from speak import speak
#import json
from Myemail import emailsender
from nasaAPI import nasa
import datetime
import meme

################################################################################################################

print('''

████████╗██╗░░██╗███████╗  ███████╗██╗░░░██╗██████╗░██╗░░░██╗
╚══██╔══╝██║░░██║██╔════╝  ██╔════╝██║░░░██║██╔══██╗╚██╗░██╔╝
░░░██║░░░███████║█████╗░░  █████╗░░██║░░░██║██████╔╝░╚████╔╝░
░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║░░░██║██╔══██╗░░╚██╔╝░░
░░░██║░░░██║░░██║███████╗  ██║░░░░░╚██████╔╝██║░░██║░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░

''')

############################################################################################################################################################
#EMAILS
siddhartEmail = 'siddharthvaish14102005@gmail.com'
vishnuEmail = 'vishnuarunkmgupta@gmail.com'
momEmail = 'archanaarunkmgupta@gmail.com'
papaEmail = 'arunkmgupta@gmail.com'
furyEmail = "thefuryassistant@gmail.com"
akshatEmail = "akshatkhare364@gmail.com"
suriEmail = "surajtiwari51234@gmail.com"
#######################################################################################################################################
def take_command():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        speak("listening")
        #r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        #audio = r.listen(source,timeout=1,phrase_time_limit=5)
        audio = r.listen(source)
        

        try:
            print('recognizeing...')
            command = r.recognize_google(audio, language='en-in')
            command = str(command).lower()
            print(f"user said: {command}")
            
            
        except Exception:
            speak("please repeat boss...")
            return''
            
        return command
#################################################################################################################
def Take_command():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        speak("listening")
        r.pause_threshold = 1
        #audio = r.listen(source,timeout=1,phrase_time_limit=5)
        audio = r.listen(source)
        

        try:
            print('recognizeing...')
            command = r.recognize_google(audio, language='en-in')
            print(f"user said: {command}")
            
            
        except Exception:
            #speak("please repeat boss...")
            return''
            
        return command

################################################################################################################################
#querry = ('volume up',"volume down", "mute",'pause',"skip","full screen","lock system",'resume',
#'back','previous video','next video','new tab','close tab','new window','show history','show download',
#'private window',"task manager","zoom in","zoom out","exit zoom","create folder","show drives","select all",
#"copy","paste",'home screen','minimize','show start','open setting','open search',"switch window",
#"take screenshot","show photo","get me new desktop")
###############################################################################################################
        
def exe(Command):
    command = str(Command)
    
    if 'time' in command:
        basic_features.tell_time()

    elif 'tomorrow date' in command:
        date_tomm()

    elif 'yesterday date' in command:
        date_yester()

    elif 'date' in command:
            tell_date()

    elif 'tell the meaning of' in command:
        mean(command)

    elif ('open' in command) and ("app" not in command):
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

    elif 'from youtube' in command:
        youtube_player(command)

    elif 'countdown' in command:
        countdown10()

    elif 'on count of three' in command:
        count_three()

    elif 'make a note' in command:
        note_maker()

    elif 'joke' in command:
        joke()

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

    elif 'send message' in command:
        command12 = command.replace('send message to ','')
        speak('whats the message for' + command12)
        mes = take_command()
        speak('sending message')
        WhatsappMsg(command12,mes)

    elif "show program files" in command:
             speak("opening")
             os.startfile("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury")

    elif"exit my files " in command:
             speak("closing Vishnu Gupta's File")
             os.system("taskkill /f /im Vishnu Gupta's File")

    elif "show my file" in command:
             npath = "C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File"
             os.startfile(npath)

    elif 'set alarm for' in command:
        #"C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\alarm.txt"
        time_to_set = str(command)
        time_now = time_to_set.replace("set alarm for ","")
        time_now = time_now.replace(" and ",":")
        time_now = time_now.replace(" ",":")
        Alarm_Time = str(time_now)
        Time_input = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\alarm.txt","a")
        Time_input.write(Alarm_Time)
        Time_input.close()

    elif 'i have a question' in command:
        speak('what is the question boss i will try to solve')
        que = take_command()
        rep = wolf_ram(que)
        speak(rep)

    elif 'calculate' in command:
        cal(command)

    elif 'temperature outside' in command:
        my_Temp()

    elif "temperature of" in command:
        command = str(command)
        command0 = command.replace('temperature of ','')
        out_temp(command0)

    elif "weather of" in command:
        command = command.replace("weather of ",'')
        weather(command)

    elif "tell weather" in command:
        weather("gorakhpur")

    elif "launch" in command:
        launch(command)

    elif "google search" in command:
        google_search(command)

    elif "look for" in command:
        look_for(command)

    elif "wallpaper" in command:
        command = command.replace("show wallpaper","")
        wallpaper(command)

    elif "internet speed" in command:
        internet_speed()

    elif "download" in  command and "movie" in command:
        movie_download(command)

    elif "photo" in command and "search" in command:
        photo_search(command)

    elif "send email" in command:
        speak("to whom boss")
        name = take_command()
        speak("what is a content")
        content = take_command()
        emailsender(name, content)

    elif "remind" in command and "later" in command:
        speak("what i have to remind")
        remind = take_command()
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

    elif ("space news" in command):
        nasa(datetime.datetime.now().strftime("%Y-%m-%d"))

    elif("make me laugh" in command) or ("i am bored" in command):
        speak("are you ready for laughing")
        meme.laugh()

    else: 
        shotcut(command)#chatbot is inside this

############################################################################################################
def run_fury():
        wish()
        while True:

                query = take_command()
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

                    if " or " in query:
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

#############################################################################################################################






     