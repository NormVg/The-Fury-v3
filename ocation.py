import pandas 
import datetime
from speak import speak
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
            if "NaN" in diloge:
                pass
            else:

                speak(diloge)
        else:
            pass




  