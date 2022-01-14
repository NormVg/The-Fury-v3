import requests
import random

from speak import speak

def weather(command):
    
    place = str(command)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid=2d1377da9da5a602d30c2a0471615967"
    #url = f"https://openweathermap.org/data/2.5/weather?q=" + place + "&appid=" + api_key_weather

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
        type = reply['weather'][0]['description']
        humi = reply['main']['humidity']
        wind = reply['wind']['speed']
        humi = str(humi)
        wind  = str(wind)
        temp = str(temp)
        speak(f"the weather of the {place} is")
        speak(f'temperature of {place} is ' + temp + 'celcius')
        speak(f'the weather of {place} is ' + type)
        speak('the humidity is ' + humi)
        speak('the wind speed is ' + wind)


