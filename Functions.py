import requests
from datetime import date
import json
date = date.today()
API_KEY='INSERT-Your_ApiKey'
def topics(topic):
    url = ('https://newsapi.org/v2/everything?'
        f'q={topic}&'
        f'from={date}&'
        'sortBy=popularity&'
        f'apiKey={API_KEY}')

    response = requests.get(url)
    news = json.loads(response.text)
    print(news)
    return news

def headlines():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=in&'
           f'apiKey={API_KEY}')
    response = requests.get(url)
    news = json.loads(response.text)
    return news
