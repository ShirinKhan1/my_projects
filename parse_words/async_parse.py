import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

async def fetch_and_parse_url(session, link):
    url = 'https://www.spreadthesign.com' + link
    async with session.get(url) as response:
        if response.status == 200:
            soup = BeautifulSoup(await response.text(), 'html.parser')
            speech_word = soup.find('div', class_='search-result-title').text.strip()
            speech_word = re.sub(r'\s+', ' ', speech_word)
            try:
                word, speech = speech_word.split(maxsplit=1)
            except ValueError:
                word = speech_word
            video_ = soup.find('div', class_='col-md-7').find('video')
            video = video_.get('src') if video_ is not None else None
            pict_div = soup.find('div', class_='col-md-5 result-image')
            pict = pict_div.find('img').get('src') if pict_div is not None else None
            audio_i = soup.find('i', class_='fa fa-volume-up js-play-audio')
            audio = audio_i.get('data-audio_url') if audio_i is not None else None
            print([word, speech, video, pict, audio])
            return [word, speech, video, pict, audio]
        else:
            print(f'Не удалось получить доступ к сайту {url}. Код ответа: {response.status}')
            return None

async def main():
    links = pd.read_csv('links.csv')
    data = []

    async with aiohttp.ClientSession() as session:
        for link in links.link:
            result = await fetch_and_parse_url(session, link)
            if result:
                data.append(result)
            await asyncio.sleep(0.2)  # Задержка 4 секунды между запросами

    data_finish = pd.DataFrame(data, columns=['word', 'speech', 'video', 'pict', 'audio'])
    data_finish.to_csv('data_finish.csv', index=False)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
