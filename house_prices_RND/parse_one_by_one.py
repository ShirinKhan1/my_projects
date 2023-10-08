# style-price-value-main-TIg6u
# params-paramsList-zLpAu          - о квартире
# style-item-address-KooqC         -местоположение
# style-item-params-list-vb1_H     - о доме
# 16519
# https://chrome.google.com/webstore/detail/adguard-adblocker/bgnkhhnnamicmpeenaelnjfhikgbkllg
import random
import time
from csv import writer
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/112.0.0.0 Safari/537.36")
driver = webdriver.Chrome('./chromedriver/chromedriver.exe')

df_links = pd.read_csv('links.csv')
df_links = df_links.drop(columns=['link'])
df_links = df_links.rename(columns={'Unnamed: 0': 'link'})
URLS = df_links['link']
property_apartment = \
    ('Количество комнат', 'Общая площадь', 'Площадь кухни', 'Жилая площадь', 'Этаж', 'Балкон или лоджия', 'Санузел',
     'Ремонт')

property_house = ('Тип дома', 'Год постройки', 'Грузовой лифт', 'Двор', 'Парковка', 'В доме')
cost = ('цена',)
location = ('адрес',)
all_ = cost + property_apartment + property_house + location
columns = list(all_)
# data_all = np.array([], 'str')

df = pd.DataFrame(data=[], columns=columns)
df.to_csv('data.csv')

file = open('data.csv', 'a', newline='')
writer_row = writer(file)


def distribution(txt, pr):
    separation = txt.split(':')
    if separation[0] in pr:
        if ord(separation[1][-1]) == 178:
            separation[1] = separation[1][:-2]
        return {separation[0]: separation[1]}


for URL, iteration in zip(URLS, range(1, len(URLS) + 1)):
    try:
        data = {}
        for prop in all_:
            data[prop] = None
        driver.get(URL)
        print(f'страница {iteration}')
        time.sleep(random.randint(2, 3))
        price = driver.find_element(By.CLASS_NAME, 'style-price-value-main-TIg6u'). \
            find_element(By.TAG_NAME, 'span').get_attribute('content')
        data.update({'цена': int(price)})

        info_apartment = driver.find_element(By.CLASS_NAME, 'params-paramsList-zLpAu').find_elements(By.TAG_NAME, 'li')
        info_location = driver.find_element(By.CLASS_NAME, 'style-item-address-KooqC').find_element(By.TAG_NAME,
                                                                                                    'div').find_element(
            By.TAG_NAME, 'span').text
        info_house = driver.find_element(By.CLASS_NAME, 'style-item-params-list-vb1_H').find_elements(By.TAG_NAME, 'li')

        for info in info_apartment:
            info_txt = distribution(info.text, property_apartment)
            if not (info_txt is None):
                data.update(info_txt)

        for info in info_house:
            info_txt = distribution(info.text, property_house)
            # print(info_txt)
            if not (info_txt is None):
                data.update(info_txt)

        data.update({'адрес': info_location})
        # print()
        # data_ = pd.DataFrame(data)
        # df = pd.concat([df, data_])
        # print(list(data.values()))
        writer_row.writerow(list(data.values()))
        # data_all = np.append(data_all, list(data.values()))

    except Exception as e:
        print('error')

    # if iteration == 3:
    #     break
# df.to_csv('data.csv')
file.close()
driver.close()
driver.quit()
