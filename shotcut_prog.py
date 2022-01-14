import pyautogui
from keyboard import press_and_release
from keyboard import write
from time import sleep
from speak import speak
from keyboard import press
from keyboard_input import take_querry
from pyautogui import leftClick
import os
import random
from ChatBot import chatbot

def shotcut(command):
        if "volume up" in command:
                 pyautogui.press("volumeup")
                 pyautogui.press("volumeup")
                 pyautogui.press("volumeup")
                 pyautogui.press("volumeup")
                 pyautogui.press("volumeup")
        elif "volume down" in command:
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
        elif "mute" in command:
                pyautogui.press("volumemute")        
        elif 'pause' in command:
                pyautogui.press('space bar')
        elif "skip" in command:
                pyautogui.press('i')
        elif "full screen" in command:
                pyautogui.press("f")
        elif "lock system" in command:
                press_and_release('windows + l')
        elif 'resume' in command:
                press('space bar')
        elif 'back' in command:
                press('j')
        elif 'previous video' in command:
                press_and_release('SHIFT + p')
        elif 'next video' in command:
                press_and_release('SHIFT + n')
        elif 'new tab' in command:
                press_and_release('ctrl + t')
        elif 'close tab' in command:                                                                                                                                                                                        
                press_and_release('ctrl + w')
        elif 'new window' in command:
                press_and_release('ctrl + n')
        elif 'show history' in command:
                press_and_release('ctrl + h')
        elif 'show download' in command:
                press_and_release('ctrl + j')
        elif 'private window' in command:
                press_and_release('Ctrl + Shift + n')
        elif "task manager" in command:
                press_and_release('ctrl + shift +esc') 
        elif "zoom in" in command:
                press_and_release('windows + =')
                sleep(1)
                press_and_release('windows + =')
        elif "zoom out" in command:
                press_and_release('windows + -')
                sleep(0.2)
                press_and_release('windows + -')
        elif "exit zoom" in command:
                press_and_release('windows + esc')
                sleep(0.2)
                press_and_release('windows + esc')
        elif "create folder" in command:
                opt = 'give the name of the folder name','folder name','name of the folder','name the folder'
                opr = random.choice(opt)
                speak(opr)
                name = take_querry()
                sleep(5)
                press_and_release('ctrl + shift + n')
                sleep(0.5)
                name = str(name)
                write(name)
                leftClick()
        elif "show drive" in command:
                press_and_release('windows + e')
        elif "select all" in command:
                press_and_release("ctrl + a")
        elif "copy"  in command:
                press_and_release("ctrl + c")
        elif "paste" in command:
                press_and_release("ctrl + v")
        elif 'home screen' in command:
                press_and_release('windows + m')
        elif 'minimize' in command:
                press_and_release('windows + m')
        elif 'show start' in command:
                press('windows')
        elif 'open setting' in command:
                press_and_release('windows + i')
        elif 'open search' in command:
                press_and_release('windows + s')
        elif "switch window" in command:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.keyUp("alt")
        elif "take screenshot" in command:
                speak("boss, please what name should i give to screenshot")
                name = take_querry()
                speak("please hold on i am taking screenshot")
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("screenshot has been taken boss")
        elif "show photo" in command:
             os.startfile("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\Photos.lnk")
        elif "get me new desktop" in command:
                pyautogui.hotkey('winleft','ctrl','d')
        else:
                chatbot(command)
