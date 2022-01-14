from plyer import notification
from playsound import playsound
from speak import speak
def notify(topic,dec):

    
    playsound("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\python fury assistant project\\Extra\\notification.mp3")              
    notification.notify(
        title = topic,
        message = dec,
        app_icon = "C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\ICO.ico",
        timeout = 10
    )
   # playsound("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\notification.mp3")

    speak(dec)
def notify2(topic,dec,say):

    
    playsound("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\python fury assistant project\\Extra\\notification.mp3")              
    notification.notify(
        title = topic,
        message = dec,
        app_icon = "C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\ICO.ico",
        timeout = 10
    )
   # playsound("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\notification.mp3")
    if "False" in say:
        pass
    else:
        speak(dec)
