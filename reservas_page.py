import logging
import os
from datetime import datetime

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ReservasPage:
    def __init__(self, driver: WebDriver, timeout: int, logger: logging.Logger) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = logger

    def _captura_pantalla(self, nombre: str) -> None:
        directorio_script = os.path.dirname(os.path.abspath(__file__))
        carpeta_capturas = os.path.join(directorio_script, "capturas")
        os.makedirs(carpeta_capturas, exist_ok=True)
        ruta = os.path.join(carpeta_capturas, f"{nombre}.png")
        self.driver.save_screenshot(ruta)
        self.logger.info(f"Captura de pantalla guardada en {ruta}")

    def open_panel_reserva(self) -> None:
        try:
            self.logger.info("Abriendo menu de reservas")
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '[data-testid="navigation-v2--book--item"]')
                )
            ).click()
        except Exception as e:
            self.logger.error(f"Error en open_panel_reserva: {e}")
            self._captura_pantalla("open_panel_reserva_error")
            raise

    def open_calendario(self) -> None:
        try:
            self.logger.info("Abriendo calendario")
            self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "calendar-icon-container"))
            ).click()
        except Exception as e:
            self.logger.error(f"Error en open_calendario: {e}")
            self._captura_pantalla("open_calendario_error")
            raise

    def select_edificio(self, edificio: str) -> None:
        try:
            self.logger.info(f"Seleccionado edificio: {edificio}")
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '[data-testid="book--office-selector"]')
                )
            ).click()
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//*[contains(text(), "{edificio}")]')
                )
            ).click()
        except Exception as e:
            self.logger.error(f"Error en select_edificio: {e}")
            self._captura_pantalla("select_edificio_error")
            raise

    def select_planta(self, planta: str) -> None:
        try:
            self.logger.info(f"Seleccionado planta: {planta}")
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '[data-testid="book--floor-selector"]')
                )
            ).click()
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//*[contains(text(), "{planta}")]')
                )
            ).click()
        except Exception as e:
            self.logger.error(f"Error en select_planta: {e}")
            self._captura_pantalla("select_planta_error")
            raise

    def select_mes(self, mes: str) -> None:
        try:
            self.logger.info(f"Ajustando mes a {mes}")
            while True:
                mes_element = self.wait.until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, '[aria-label="Choose Month"]')
                    )
                )
                mes_actual = mes_element.text

                if mes == mes_actual:
                    break

                self.wait.until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, '[aria-label="Next Month"]')
                    )
                ).click()
        except Exception as e:
            self.logger.error(f"Error en select_mes: {e}")
            self._captura_pantalla("select_mes_error")
            raise

    def select_dia(self, fecha: datetime) -> None:
        try:
            testid = fecha.strftime("%Y-%m-%d")
            self.logger.info(f"Seleccionando dia {testid}")
            dia_element = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, f'[data-testid="{testid}"]')
                )
            )
            self.driver.execute_script("arguments[0].click();", dia_element)
        except Exception as e:
            self.logger.error(f"Error en select_dia: {e}")
            self._captura_pantalla("select_dia_error")
            raise

    def select_hora_inicio(self, start: str) -> None:
        try:
            self.logger.info(f"Seleccionando hora de inicio {start}")
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '[data-testid="book--time-picker-start"]')
                )
            ).click()
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//*[contains(text(), "{start}")]')
                )
            ).click()
        except Exception as e:
            self.logger.error(f"Error en select_hora_inicio: {e}")
            self._captura_pantalla("select_hora_inicio_error")
            raise

    def select_hora_fin(self, end: str) -> None:
        try:
            self.logger.info(f"Seleccionando hora de fin {end}")
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '[data-testid="book--time-picker-end"]')
                )
            ).click()
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//*[contains(text(), "{end}")]')
                )
            ).click()
        except Exception as e:
            self.logger.error(f"Error en select_hora_fin: {e}")
            self._captura_pantalla("select_hora_fin_error")
            raise

    def unselect_dia_completo(self) -> None:
        try:
            self.logger.info("Desactivando 'Todo el dia'")
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '[data-testid="book--switch-full-day"]')
                )
            ).click()
        except Exception as e:
            self.logger.error(f"Error en unselect_dia_completo: {e}")
            self._captura_pantalla("unselect_dia_completo_error")
            raise

    def confirm_reserva(self) -> None:
        try:
            self.logger.info("Confirmando reserva")
            cards = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, '[data-testid="booking-suggestions-card"]')
                )
            )
            favourite_card = None
            for i, card in enumerate(cards):
                if "Favourite" in card.text:
                    favourite_card = card
                    break

            if not favourite_card:
                raise Exception("Error al encontrar la carta favorita")

            quick_book_btn = favourite_card.find_element(
                By.XPATH, './/*[contains(text(), "Quick book")]'
            )
            self.wait.until(EC.element_to_be_clickable(quick_book_btn)).click()

        except Exception as e:
            self.logger.error(f"Error en confirm_reserva: {e}")
            self._captura_pantalla("confirm_reserva_error")
            raise

    def get_confirm_reserva(self) -> bool:
        try:
            self.logger.info("Obteniendo mensaje de confirmacion")

            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[contains(text(), "Booked")]')
                )
            )
            return True
        except TimeoutException:
            self.logger.info("No se encontró texto 'Booked'")
            return False
        except Exception as e:
            self.logger.error(f"Error en get_confirm_reserva: {e}")
            self._captura_pantalla("get_confirm_reserva_error")
            raise
