from selenium import webdriver

from settings import *

def iniciar_driver():
    driver = webdriver.Chrome()
    driver.get(URL)
    return driver

def reservar():
    print("buenas")
    iniciar_driver()

