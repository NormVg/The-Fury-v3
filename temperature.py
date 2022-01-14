from speak import speak
import requests
from bs4 import BeautifulSoup
import random


def my_Temp():
    
    
    place = str("gorakhpur")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid=2d1377da9da5a602d30c2a0471615967"
    link = requests.get(url)

    reply = link.json()
    #print(reply)

    if reply['cod'] == '404':
        print("city not found in the database")
        rs = f"there is no weather data city named {place} boss. please check the city",f'i could not get informatiom of weather of {place}',f'weather of {place}  not found','cant not get the information','i am sorry boss can not the the information'
        rp = random.choice(rs)
        speak(rp)


    else:
        temp = ((reply['main']['temp'])) #- 273.15)
      
        temp = str(temp)
        speak(f'temperature of {place} is ' + temp + 'celcius')

def out_temp(command):

    place = str(command)

    url = f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid=2d1377da9da5a602d30c2a0471615967"
    link = requests.get(url)

    reply = link.json()
    #print(reply)

    if reply['cod'] == '404':
        print("city not found in the database")
        


    else:
        temp = ((reply['main']['temp'])) #- 273.15)
      
        temp = str(temp)
        speak(f'temperature of {place} is ' + temp + 'celcius')
