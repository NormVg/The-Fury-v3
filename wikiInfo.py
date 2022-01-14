import requests
import bs4

def infom(command):

    okk = requests.get(f"https://en.wikipedia.org/wiki/{command}")

    if okk is not None:

        page = bs4.BeautifulSoup(okk.text,"html.parser")

        title = page.select("#firstHeading")[0].text
        paragraph = page.select("p")

        print(title)
        intro = "\n".join([ para.text for para in paragraph[0:5]])

        par = intro.split(".", maxsplit= 3)
        main = f"{par[0]}. {par[1]}. {par[2]}."
        print(main)
        
        return main,title

