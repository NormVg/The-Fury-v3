from speak import speak
import requests
import os 



def nasa(Date):
    Date = str(Date)

    date = Date.replace(" and ","-")
    date = date.replace(" and ","-")
    date = date.replace(" and ","-")


    nasa_api = "sAUrd9k9hv74XOjsGN6C2Mrhq0TogvGzFbTfTYye"

    
    speak("Extracting Data From Nasa database . ")

    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(nasa_api)

    oac = {'date':str(date)}
    
    r = requests.get(Url,params = oac)

    Data = r.json()
    print(Data)
    Info = Data['explanation']

    Title = Data['title']

    Image_Url = Data['url']


    Image_r = requests.get(Image_Url)

    FileName = str(date) + '.jpg'

    with open(FileName,'wb') as f:

        f.write(Image_r.content)

    Path_1 = "C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\" + str(FileName)

    Path_2 = "C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\" + str(FileName)

    os.rename(Path_1, Path_2)

    os.startfile(Path_2)

    #img = Image.open(Path_2)

    #img.show()

    print(f"{Title}")
    print(f"{Info}")
    speak(f"Title : {Title}")
    speak(f"According To Nasa database : {Info}") 
    
    os.remove(Path_2)

