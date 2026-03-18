from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import logging

from settings import *

logging.basicConfig(
    level=getattr(logging, LOGGING_LEVEL),
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

def options_navegador():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    if HEADLESS:
        options.add_argument("--headless=new")

    return options

def iniciar_driver():
    logging.info("Iniciando navegador")
    
    try:

        driver = webdriver.Chrome(options=options_navegador())
        driver.get(URL)

        # Esperar a que cargue la pagina
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))

        return driver
    
    except Exception as e:
        logging.error(f"Error al iniciar el navegador: {e}")
        return None

def reservar():
    logging.info("Iniciando proceso de reserva")
    
    driver = iniciar_driver()

    if driver is None:
        logging.error("No se pudo iniciar el navegador. Abortando proceso de reserva")
        return
    
    logging.info("Reserva finalizada")

