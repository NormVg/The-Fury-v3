import datetime
from speak import speak
from time import sleep


#extracting date
extracted_time = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\after a long time.txt",'rt')
time = extracted_time.read()
Time = str(time)

#delete_time = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\python fury assistant project\\Data.txt",'r+')
#delete_time.truncate(0)
#delete_time.close()

def lastTimeSaver():
    today = datetime.datetime.now().strftime('%d-%m')
    Time_input = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\after a long time.txt","a")
    Time_input.write(today)
    Time_input.close()

def lastTimedelete():
    delete_time = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\after a long time.txt",'r+')
    delete_time.truncate(0)
    delete_time.close()

def last_time():
    extracted_time = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\after a long time.txt",'rt')
    time = extracted_time.read()
    Time = str(time)
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
