import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

links = pd.read_csv('links.csv')
data = []
# link = links.link[0]
for link in links.link:
    response = requests.get('https://www.spreadthesign.com' + link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # links_word = soup.find('div', class_="col-sm-4 search-results").find_all('a')
        # print(response.text)
        speech_word = soup.find('div', class_='search-result-title').text.strip()
        speech_word = re.sub(r'\s+', ' ', speech_word)
        try:
            word, speech = speech_word.split(maxsplit=1)
        except ValueError:
            word = speech_word
        video_ = soup.find('div', class_='col-md-7').find('video')
        if not (video_ is None):
            video = video_.get('src')
        else:
            video = None
        pict_div = soup.find('div', class_='col-md-5 result-image')
        if not (pict_div is None):
            pict = pict_div.find('img').get('src')
        else:
            pict = None
        audio_i = soup.find('i', class_='fa fa-volume-up js-play-audio')
        if not (audio_i is None):
            audio = audio_i.get('data-audio_url')
        else:
            audio = None
        print([word, speech, video, pict, audio])
        data.append([word, speech, video, pict, audio])
        # print(data)
    else:
        print('Не удалось получить доступ к сайту. Код ответа:', response.status_code)
data_finish = pd.Series(data)
df = data_finish.to_frame()
df.columns = ['word', 'speech', 'video', 'pict', 'audio']
df.to_csv('data_finish.csv')
