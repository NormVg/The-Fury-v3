from os import startfile
from time import sleep
from pyautogui import click
from keyboard import write
from keyboard import press


def WhatsappMsg(name,message):

    
    
    #web.open('https://web.whatsapp.com/')
     
    startfile("C:\\Users\\Arun Gupta\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp\\WhatsApp")

    sleep(24)

    click(x=251, y=110)

    sleep(1.5)
    
    write(name)

    sleep(1)

    click(x=273, y=239)

    sleep(1)

    click(x=751, y=698)

    sleep(1)

    write(message)

    press('enter')

