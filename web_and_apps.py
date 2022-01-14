import webbrowser
from speak import speak
from keyboard import press_and_release
from time import sleep
from keyboard import write
from pyautogui import click
from pyautogui import press
import speedtest
from keyboard_input import take_querry
from listen import take_command
import random
import wikipedia
import wolframalpha
from pyautogui import hotkey
from pytube import YouTube
from pyperclip import paste
import pywhatkit
import pyperclip
#from THE_FURY import Take_command
def launch(command):
    name = command.replace("launch","")
    web = 'https://www.' + name + '.com'  #######
    webbrowser.open(web)
    speak(f"launching {name} boss")

def look_for(command):
    command = command.replace("look for ","")
    url = (f"https://www.amazon.in/s?k={command}&ref=nb_sb_noss_2")##############
    webbrowser.open(url)
    speak(f"this what i found for {command} on amazon")

def app_opener(command):
    open = command.replace('open',"")##############
    speak(f'opening {open} boss')     
    press_and_release("windows + s")
    sleep(1)
    click(x=150, y=706)
    write(open)
    sleep(1)
    press("enter")

def google_search():
    speak("what should i search boss")#$$$$$$$$$$$$$$$$
    search = take_querry()
    webbrowser.open(f'https://www.google.com/search?q={search}')

def wallpaper(command):
    speak('searching from wallpaper cave')
    webbrowser.open(f'https://wallpapercave.com/search?q={command}+laptop')##################

def internet_speed():
    try:
        speak("cheaking boss please wait")
        st = speedtest.Speedtest()
        download = st.download()
        down = int(download/800000)
        upload = st.upload()#######################
        up = int(upload/800000)
        speak(f"boss we have {down} mb per second downloding and {up} mb per second uploding speed")
        print(down + "mbps")
        print(up + "mbps")
            
    except:
        speak('can not get the internet speed boss')

def youtube_player(command):
    command = str(command)####################
    video = command.replace('play','')
    video = command.replace('from youtube','')
    print(video)
    rn = f'playing {video} on youtube',"playing","playing as you said boss"
    rn = random.choice(rn)
    speak(rn)
    pywhatkit.playonyt(video)

def wolf_ram(command):
    
    api_id = "4ELXPQ-3RHHU87E6W"

    rq = wolframalpha.Client(api_id)

    rqt = rq.query(command)

    try:
        ans = next(rqt.results).text

        return ans

    except:
        speak(f"can not find result for {command} in database")

def download_youtube():
    
    sleep(1)

    click(x=604, y=48)

    hotkey('ctrl','c')#####################

    url = pyperclip.paste()

    Link = str(url)

    def download(link):

        url1 = YouTube(link)
        ans = take_command()
        if 'with video' in ans:

            video = url1.streams.get_lowest_resolution()
            video.download("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\")
        elif 'only audio' in ans:
            video = url1.streams.get_audio_only()
            video.download("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\")



    download(Link) 
    speak("downloaded boss")

def cal(command):
    que = str(command)

    que1 = que.replace('calculate ','')

    que = que1.replace("plus","+")
    que = que.replace("minus","-")###################
    que = que.replace("into","*")
    que = que.replace("by","/")
    que = que.replace("divided by","/")
    final = str(que)
    try:
        sol = wolf_ram(final)
        speak(f"boss answer of your mathematical question is {sol}")
        print(sol)
    except:
        speak(f"i am not able to find answer of {que1}")

def movie_download(command):################################
    command = str(command)
    command = command.replace('see for ','')
    command = command.replace(' movie','')
    webbrowser.open(f'https://moviesverse.cc/?s={command}')

def photo_search(command):################################
    command = str(command)
    command = command.replace('search for','')
    command = command.replace('photo','')
    webbrowser.open(f'https://www.google.com/search?q={command}&sxsrf=AOaemvJxTNg4vXa-TtkshHhnbKcVcl3lwg:1639380037483&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiipqTGnuD0AhXf63MBHXfmAvsQ_AUoAXoECAIQAw&cshid=1639380057355122&biw=1366&bih=657&dpr=1')

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

def help_concentrate():
    webbrowser.open("https://rainymood.com")
    sleep(17)
    click(x=698, y=198)

def image_match():
    url = "https://www.google.com/imghp?hl=en"
    webbrowser.open(url)