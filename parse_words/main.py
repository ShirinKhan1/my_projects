import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL = "https://www.spreadthesign.com/ru.ru/search/by-category/"
list_URL = [
    'https://www.spreadthesign.com/ru.ru/search/by-category/398/zhestovyi-iazyk-dlia-nachinaiushchikh/',
    'https://www.spreadthesign.com/ru.ru/search/by-category/1/obshchie-polozheniia/',
    'https://www.spreadthesign.com/ru.ru/search/by-category/37/predlozheniia/',
    'https://www.spreadthesign.com/ru.ru/search/by-category/86/religiia/',
    'https://www.spreadthesign.com/ru.ru/search/by-category/28/iazyk/',
    'https://www.spreadthesign.com/ru.ru/search/by-category/113/iskusstvo-i-razvlecheniia/',
    'https://www.spreadthesign.com/ru.ru/search/by-category/46/sotsialnye-issledovaniia/',
    'https://www.spreadthesign.com/ru.ru/search/by-category/99/geografiia-i-puteshestviia/',
    'https://www.spreadthesign.com/ru.ru/search/by-category/125/eda-i-napitki/',
    'https://www.spreadthesign.com/ru.ru/search/by-category/68/stil-zhizni/',
    'https://www.spreadthesign.com/ru.ru/search/by-category/147/sport-i-otdykh/',
    'https://www.spreadthesign.com/ru.ru/search/by-category/213/tekhnologiia/',
    'https://www.spreadthesign.com/ru.ru/search/by-category/227/kompiuter-i-sovremennye-tekhnologii/1',
    'https://www.spreadthesign.com/ru.ru/search/by-category/168/nauka/',
    'https://www.spreadthesign.com/ru.ru/search/by-category/194/zdorove-i-meditsina/',
    'https://www.spreadthesign.com/ru.ru/search/by-category/255/zhesty-malyshei/'
]
num = 0
links = []
for url in list_URL:
    print(url)
    next_ = True
    p = 1
    while next_:
        print(p)
        response = requests.get(url+f'?q=&p={p}')
        # Проверяем успешность запроса
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links_word = soup.find('div', class_="col-sm-4 search-results").find_all('a')
            if not links_word:
                next_ = False
            for a_tag in links_word:
                href = a_tag.get('href')
                if not href[0] == '?':
                    links.append(href)

        else:
            next_ = False
            print('Не удалось получить доступ к сайту. Код ответа:', response.status_code)
        p += 1

links = pd.Series(links)
df = links.to_frame()
df.to_csv('links.csv')

