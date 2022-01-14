import os
import time
from keyboard import write
from pyautogui import press,click
from keyboard import press_and_release

def alarm(command,date):
    
    time_to_set = str(command)
    
    time_now = time_to_set.replace("set alarm for ","") 
    time_now = time_now.replace(" and ",":")
    time_now = time_now.replace(" ",":")

    Alarm_Time = str(time_now)

    os.startfile("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\Free Alarm Clock.lnk")
    time.sleep(1.5)
    press_and_release('ctrl + n')
    time.sleep(.7)
    write(Alarm_Time)
    time.sleep(.5)
    click(x=781, y=217)
    write(date)
    time.sleep(.4)
    press('enter')
    time.sleep(.4)
    click(x=1348, y=13)
    



