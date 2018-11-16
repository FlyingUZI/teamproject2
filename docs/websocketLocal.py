import time  #time

from websocket import create_connection  #websocket

#scraping

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select

#ws = create_connection("ws://35.236.39.253:80/ws")
#result = None

while (1):
    ws = create_connection("ws://35.236.39.253:80/ws")
    result = None
    #contnue return
    while (result != "open"):
        result = ws.recv()
        time.sleep(1)
        print("test")

    #ws.send("Opened")
    time.sleep(1)
    ws.close()
    continue
