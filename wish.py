import datetime
import random
from eventManager import *
from last_time import last_time
from speak import speak


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
    birthday_Reminder()
    birthday_tell()

    

