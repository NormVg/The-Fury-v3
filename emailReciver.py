import easyimap
import datetime
from speak import speak
from listen import take_command
import webbrowser
#####################################
now = datetime.datetime.now()
user1 = "thefuryassistant@gmail.com"
password = "gameisworld4me"
host = "imap.gmail.com"
user2 = 'vishnuarunkmgupta@gmail.com'
user1file = ("lastEmailTime1")
user2file = ("lastEmailTime2")
link = "https://accounts.google.com/signin/v2/identifier"
######################################

def lastTimeSaver(file,time):
    today = datetime.datetime.now().strftime('%d-%m')
    Time_input = open(f"C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\{file}.txt","a")
    Time_input.write(time)
    Time_input.close()
def lastTimedelete(file):
    delete_time = open(f"C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\{file}.txt",'r+')
    delete_time.truncate(0)
    delete_time.close()
def lastextrator(file):
    extracted_time = open(f"C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\{file}.txt",'rt')
    time = extracted_time.read()
    Time = str(time)
    return Time
def reciver():
    server = easyimap.connect(host,user1,password)
    email = server.mail(server.listids()[0])
    mailTime1 = str(email.date)
    exTIME1 = lastextrator(user1file)
    if (mailTime1 == exTIME1):
        print('no new mail')
    else:
        speak("boss you got a new male from " + str(email.from_addr))
        print("title : " + str(email.title))
        speak("title : " + str(email.title))
        lastTimedelete(user1file)
        lastTimeSaver(user1file,mailTime1)
        speak("do you want to see mail")
        com = take_command()
        if ("yes" in com) and ("sure" in com)and ("why not" in com):
            url = "https://accounts.google.com/signin/v2/identifier"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
            webbrowser.get(chrome_path).open_new(url)
            speak("please login your acount to see mail")
        elif ("no" in com) and ("not now" in com):
            pass 
    server.quit()
    #########################################################################################
    server2 = easyimap.connect(host,user2,password)
    email2 = server2.mail(server2.listids()[0])
    mailTime2 = str(email2.date)
    exTIME2 = lastextrator(user2file)
    if (mailTime2 == exTIME2):
        print('no new mail')
    else:
        speak("boss you got a new male from " + str(email2.from_addr))
        print("title : " + str(email2.title))
        speak("title : " + str(email2.title))
        lastTimedelete(user2file)
        lastTimeSaver(user2file,mailTime2)
        speak("do you want to see mail")
        com1 = take_command()
        if ("yes" in com1) and ("sure" in com1)and ("why not" in com1):
            url = "https://accounts.google.com/signin/v2/identifier"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
            webbrowser.get(chrome_path).open_new(url)
            speak("please login your acount to see mail")
        elif ("no" in com1) and ("not now" in com1):
            pass         
    server2.quit()
