#!/usr/bin/env python
# pip freeze > req.txt
# pip install -r req.txt
# pyinstaller main.py --onefile --icon="icon.ico"

#### Импорт библиотек

import requests
from bs4 import BeautifulSoup
import json
import csv
import time
from datetime import datetime
from selenium import webdriver
#from seleniumwire import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.service import Service
import time


URL = 'https://www.google.ru/'

def get_content():
    # options
    options = webdriver.ChromeOptions()

    # user-agent
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

    driver = webdriver.Chrome(
        executable_path=r"/home/vladimir/PycharmProjects/FL_artnum/chromedriver",
        options=options
    )
    try:
        driver.get(url=URL)
        time.sleep(3)
        #find_input = driver.find_element("gLFyf gsfi")

        find_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input')
        artikul = "8809647114819"
        find_input.send_keys(artikul)
        find_input.send_keys(Keys.ENTER)
        time.sleep(2)
        google_img = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[4]/a').click()
        img = driver.find_element(By.TAG_NAME, 'img')
        src = img.get_attribute('src')
        print(src)
        #driver.save_screenshot(f"{artikul}.png")
        #src = img.get_attribute('src')
        #urllib.urlretrieve(src, f"{artikul}.png")


        #driver.refresh() обновление окна браузера
        time.sleep(15)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_content()


if __name__ == '__main__':
    main()












