import requests
import json
from speak import speak



def news():
    news_api_key = "26fefdc6fb6546f2a9f9fb22a7a84668"
    url = f'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey={news_api_key}'
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak('the Source is: The Times Of India')
    speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        speak(articles['title'])
        if index == len(arts)-1:
            break
        speak('Moving on the next news headline..')
    speak('These were the top headlines, Have a nice day Sir!!..')
    
