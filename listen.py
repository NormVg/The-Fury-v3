import speech_recognition as sr
from speak import speak

def take_command():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        speak("listening")
        #r.pause_threshold = 1
        audio = r.listen(source)
        

        try:
            print('recognizeing...')
            command = r.recognize_google(audio, language='en-in')
            print(f"user said: {command}")
            command = str(command).lower()
            
            
        except Exception:
            speak("please repeat boss...")
            return"none"
            
	    #command = str(command).lower()
        return command
