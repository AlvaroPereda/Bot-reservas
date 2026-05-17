from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import logging
from datetime import datetime, timedelta

from reservas_page import ReservasPage
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
    
def es_finde_semana(fecha):
    return fecha.weekday() >= 5

def es_dia_teletrabajo(fecha): 
    return fecha.weekday() in HOME

def obtener_mes(fecha):
    return MESES[fecha.month - 1]

def reservar():
    logging.info("Iniciando proceso de reserva")
    
    driver = iniciar_driver()

    if driver is None:
        logging.error("No se pudo iniciar el navegador. Abortando proceso de reserva")
        return
    
    hoy = datetime.now()
    reserva_page = ReservasPage(driver, TIMEOUT, logging)

    try:
        for reserva in RESERVAS:
            fecha_objetivo = hoy + timedelta(days=reserva.dias_anticipacion)

            if es_finde_semana(fecha_objetivo):
                logging.info("La fecha objetivo cae en fin de semana. Saltando reserva para esa fecha")
                continue

            if es_dia_teletrabajo(fecha_objetivo):
                logging.info("La fecha objetivo es un día de teletrabajo. Saltando reserva para esa fecha")
                continue
            
            mes_nombre = obtener_mes(fecha_objetivo)

            try: 
                reserva_page.open_panel_reserva()
                reserva_page.select_edificio(reserva.edificio)
                reserva_page.select_planta(reserva.planta)
                reserva_page.open_calendario()
                reserva_page.select_mes(mes_nombre)
                reserva_page.select_dia(fecha_objetivo)
                reserva_page.unselect_dia_completo()
                reserva_page.select_hora_inicio(reserva.hora_inicio)
                reserva_page.select_hora_fin(reserva.hora_fin)
                reserva_page.confirm_reserva()
                if reserva_page.get_confirm_reserva():
                    logging.info(f"Reserva realizada con éxito para el día {fecha_objetivo.strftime('%Y-%m-%d')}")
            except Exception as e:
                logging.error(f"Error en la reserva del día {fecha_objetivo.strftime('%Y-%m-%d')}: {e}")
            
        logging.info("Reservas finalizadas")

    except Exception as e:
        logging.error(f"Error fatal inesperado: {e}")
    finally:
        driver.quit()

