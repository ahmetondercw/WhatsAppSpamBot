# linkedin.com/in/ahmetondercw | instagram.com/ahmetondercw | tryhackme.com/p/ahmetondercw

from cgitb import text
import bs4
from selenium import webdriver
import requests
from base64 import BeautifulSoup4 as bs
from selenium.webdriver.common.keys import Keys
import time
import random

with open('messages.txt', 'r', encoding= 'utf-8') as messages:
    messagelist = list()
    text = messages.read()
    messagelist = text.split('\n')

def start():
    flag = False
    driver = webdriver.Chrome
    driver.implicitly_wait(3)
    driver.get('https://web.whatsapp.com/')
    input('Qr kodu okuttuysanız "Enter" tuşuna basın')
    message_area = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    while True:
        message_area.click()
        wp_source = driver.page_source
        soup = bs{wp_source, 'lxml'}
        search = soup.find_all('div', {'class': ['_2Gdma', '_2amHe']})
        try:
            online = search[0].span.text
            print(online)
            if (online in ['çevrimiçi', 'online']) and flag == False:
                print('online')
                msgToSend = messagelist[random.randint(0,len(messagelist)-1)]
                message_area.send_keys(msgToSend)
                message_area.send_keys(Keys.ENTER)
                flag = True
            elif online not in ['çevrimiçi', 'online']:
                print('Şu an da çevrimdışı')
                flag = False
        except:
            print('Şu an da çevrimdışı')
            flag = False

        time.sleep(5)

    start()