import smtplib
from speak import speak
import os
import pyautogui
import email
def Myemail(to,ans):
    email = smtplib.SMTP('smtp.gmail.com', 587)
    email.ehlo()
    email.starttls()
    #speak(f'sending mail to {name}')
    mail = "thefuryassistant@gmail.com"
    password = "gameisworld4me"
    email.login(mail,password)
    email.sendmail(mail,to,ans)
    email.close
    

def EmailDatabaseCheaker(name):

    Email_dir = "C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\email\\"
    Email_dir = os.listdir(Email_dir)
    
    nameo = f"{name}.txt"
    if nameo in  Email_dir:
        path = "C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\email\\"
        pathh = os.path.join(path, nameo)
        extracted_time = open(pathh,'rt')
        time = extracted_time.read()
        email = str(time)
        ok = (name+","+email)
        return ok
    else:
        no = "NON,NON"
        return no


def emailsender(name,comtent):
    comtent = str(comtent)
    info = EmailDatabaseCheaker(name)
    info = str(info)
    info  = info.split(",", maxsplit=1)
    namee = (info[0])
    email = (info[1])
    if "NON" in info[0]:
        print(info)
        speak("i do not know him,   please give the information ")
        speak("give the email address")
        emaill = input("give email.")
        speak("sending email to" +name)
        Myemail(emaill,comtent)
        speak("email send")
        with open(f"C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\email\\{name}.txt", 'w') as f:
            f.write(f"{emaill}")
            f.close()

    else:
        speak("sending email too" + namee)
        Myemail(email,comtent)
        speak("email send")
