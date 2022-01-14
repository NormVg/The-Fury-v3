import requests
import bs4,os,time,password_genrator
def laugh():
    for i in range(10):
        request = requests.get("https://imgflip.com/i/")
        soup = bs4.BeautifulSoup(request.text, "html.parser")
        try:
            img_url = 'https:'+ soup.find('img', id = "im")['src']
        except:
            img_url = 'https:'+ soup.find('video', id = "vid")['poster']

        Image_r = requests.get(img_url)
        FileName = str(password_genrator.gen()) + '.jpg'

        with open(FileName,'wb') as f:
            f.write(Image_r.content)

            #Path_1 = "C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\" + str(FileName)

            #Path_2 = "C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\" + str(FileName)

        #os.rename(Path_1, Path_2)

        os.startfile(FileName)
        time.sleep(5)
        os.remove(FileName)
