import pandas 
import datetime
from whatsapp_auto_message import WhatsappMsg
from speak import speak
from notification import notify2
import time


def ocation():
    df = pandas.read_excel("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\Ocation.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")

    for index, item  in df.iterrows():
        oday = item['date'].strftime("%d-%m")

        if  (today == oday):
            ocation = item['ocation']
            diloge = item['diloge']
            speak(f"boss today is {ocation}")
            time.sleep(.5)
            if ("NaN" in str(diloge)):
                pass
            else:

                speak(diloge)
        else:
            pass


def birthday_Reminder():
    df = pandas.read_excel("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\birthdaySender.xlsx")
    presentday = datetime.datetime.now()
    tommor = presentday + datetime.timedelta(1)
    tommor = tommor.strftime("%d-%m")

    for index, item  in df.iterrows():
        oday = item['date'].strftime("%d-%m")
        #ylast = item['year']
        if  (tommor == oday) :
            name = item['name']
            notify2("Birthday reminder",f"boss tomorrow is {name} birthday",say= "False")
            speak(f'boss tomorrow is {name} birthday')
        else:
            pass

def birthday_tell():
    df = pandas.read_excel("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\birthdaySender.xlsx")
    presentday = datetime.datetime.now().strftime('%d-%m')
    yearN = datetime.datetime.now().strftime("%Y")
    writeInd = []
    for index, item  in df.iterrows():
        oday = item['date'].strftime("%d-%m")
        ylast = item['year']
        if  (presentday == oday) and ( str(yearN) not in str(ylast)):
            name = item['name']
            if "boss" in name:
                speak("happy birthday boss")
            else:
                speak(f'boss today is {name} birthday')
            writeInd.append(index)

        else :
            pass

    for i in writeInd:
        yr = df.loc[i,'year']
        df.loc[i,'year'] = f"{str(yr)} , {str(yearN)}"
        df.to_excel("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\birthdaySender.xlsx",index= False)
