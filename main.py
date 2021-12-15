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
from fake_useragent import UserAgent
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
        executable_path=r"C:\Users\Vladimir\PycharmProjects\FL_artnum\chromedriver.exe",
        options=options
    )
    try:
        driver.get(url=URL)
        time.sleep(3)
        find_input = driver.find_element("gLFyf gsfi")
        #find_input = driver.find_element(value='[title="Поиск"]') #value = '[name="%s"]'
        find_input.send_keys("8809647114819")
        # find_input.send_keys(Keys.ENTER)
        #driver.refresh() обновление окна браузера
        time.sleep(100)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_content()


if __name__ == '__main__':
    main()












