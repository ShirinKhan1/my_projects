from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
from csv import writer
import numpy as np
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
# 47.22880257383533, 39.71605027022914 - центр
URL = 'https://www.avito.ru/rostov-na-donu/kvartiry/prodam-ASgBAgICAUSSA8YQ?p=1'
driver = webdriver.Chrome('./chromedriver/chromedriver.exe')
data = []
df = pd.DataFrame(data=data, columns=['link'])
df.to_csv(r'links.csv')
file = open('links.csv', 'a', newline='')
writer = writer(file)
try:
    for _ in range(1, 100):
        driver.get(URL)
        time.sleep(3)
        print(f'страница {_}')
        blocks = driver.find_element(By.CLASS_NAME, 'items-items-kAJAg')
        apartments = blocks.find_elements(By.TAG_NAME, 'div')

        for apartment in apartments:
            if len(apartment.get_attribute('id')) == 11:
                apartment_link = apartment. \
                    find_element(By.CLASS_NAME, 'iva-item-content-rejJg'). \
                    find_element(By.CLASS_NAME, 'iva-item-body-KLUuy'). \
                    find_element(By.CLASS_NAME, 'iva-item-titleStep-pdebR'). \
                    find_element(By.TAG_NAME, 'a').get_attribute('href')
                data.append(apartment_link)
        print('Загружем данные в csv')
        for link in data:
            writer.writerow([link])
        print('Переход на следующую страницу')
        pagination = driver.find_element(By.CLASS_NAME, 'styles-module-root-OK422')
        pag_blocks = pagination.find_elements(By.TAG_NAME, 'li')
        pag_blocks[-1].click()
        URL = f'https://www.avito.ru/rostov-na-donu/kvartiry/prodam-ASgBAgICAUSSA8YQ?p={_ + 1}'

except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
