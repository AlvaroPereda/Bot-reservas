import logging
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from reservas_page import ReservasPage
from settings import *

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=getattr(logging, LOGGING_LEVEL),
    format="%(asctime)s - [%(levelname)s] - %(message)s",
)


def options_navegador():
    options = Options()
    options.binary_location = CHROMIUM_BINARY
    if CHROME_USER_DATA_DIR:
        options.add_argument(f"--user-data-dir={CHROME_USER_DATA_DIR}")
        options.add_argument(f"--profile-directory={CHROME_PROFILE}")
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    return options


def iniciar_driver():
    logger.info("Iniciando navegador")

    try:
        service = Service(CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=options_navegador())
        driver.get(URL)

        # Esperar a que cargue la pagina
        WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )

        return driver

    except Exception as e:
        logger.error(f"Error al iniciar el navegador: {e}")
        return None


def es_finde_semana(fecha):
    return fecha.weekday() >= 5


def es_dia_teletrabajo(fecha):
    return fecha.weekday() in HOME


def obtener_mes(fecha):
    return MESES[fecha.month - 1]


def reservar():
    logger.info("Iniciando proceso de reserva")

    driver = iniciar_driver()

    if driver is None:
        logger.error("No se pudo iniciar el navegador. Abortando proceso de reserva")
        return

    hoy = datetime.now()
    reserva_page = ReservasPage(driver, TIMEOUT, logger)

    try:
        for reserva in RESERVAS:
            fecha_objetivo = hoy + timedelta(days=reserva.dias_anticipacion)

            if es_finde_semana(fecha_objetivo):
                logger.info(
                    "La fecha objetivo cae en fin de semana. Saltando reserva para esa fecha"
                )
                continue

            if es_dia_teletrabajo(fecha_objetivo):
                logger.info(
                    "La fecha objetivo es un día de teletrabajo. Saltando reserva para esa fecha"
                )
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
                    logger.info(
                        f"Reserva realizada con éxito para el día {fecha_objetivo.strftime('%Y-%m-%d')}"
                    )
            except Exception as e:
                logger.error(
                    f"Error en la reserva del día {fecha_objetivo.strftime('%Y-%m-%d')}: {e}"
                )

        logger.info("Reservas finalizadas")

    except Exception as e:
        logger.error(f"Error fatal inesperado: {e}")
    finally:
        driver.quit()
