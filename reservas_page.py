from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os

class ReservasPage:

    def __init__(self, driver, timeout, logging):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logging = logging

    def _captura_pantalla(self, nombre):
        os.makedirs("capturas", exist_ok=True)
        ruta = os.path.join("capturas", f"{nombre}.png")
        self.driver.save_screenshot(ruta)
        self.logging.info(f"Captura de pantalla guardada en {ruta}")

    def open_panel_reserva(self):
        try:
            self.logging.info("Abriendo menu de reservas")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="navigation--book--item"]'))).click()
        except Exception as e:
            self.logging.error(f'Error en open_panel_reserva: {e}')
            self._captura_pantalla("open_panel_reserva_error")
            raise

    def open_calendario(self):
        try:
            self.logging.info("Abriendo calendario")
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "calendar-icon-container"))).click()
        except Exception as e:
            self.logging.error(f'Error en open_calendario: {e}')
            self._captura_pantalla("open_calendario_error")
            raise
    
    def select_edificio(self, edificio):
        try:
            self.logging.info(f'Seleccionado edificio: {edificio}')
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="book--office-selector"]'))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[contains(text(), "{edificio}")]'))).click()
        except Exception as e:
            self.logging.error(f'Error en select_edificio: {e}')
            self._captura_pantalla("select_edificio_error")
            raise
    
    def select_planta(self, planta):
        try:
            self.logging.info(f'Seleccionado planta: {planta}')
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="book--floor-selector"]'))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[contains(text(), "{planta}")]'))).click()
        except Exception as e:
            self.logging.error(f'Error en select_planta: {e}')
            self._captura_pantalla("select_planta_error")
            raise

    def select_mes(self, mes):
        try:
            self.logging.info(f'Ajustando mes a {mes}')
            while True:
                mes_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="Choose Month"]')))
                mes_actual = mes_element.text

                if mes == mes_actual:
                    break

                self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Next Month"]'))).click()
        except Exception as e:
            self.logging.error(f'Error en select_mes: {e}')
            self._captura_pantalla("select_mes_error")
            raise
    
    def select_dia(self, fecha):
        try:
            testid = fecha.strftime("%Y-%m-%d")
            self.logging.info(f'Seleccionando dia {testid}')
            dia_element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[data-testid="{testid}"]')))
            self.driver.execute_script("arguments[0].click();", dia_element)
        except Exception as e:
            self.logging.error(f'Error en select_dia: {e}')
            self._captura_pantalla("select_dia_error")
            raise

    def select_hora_inicio(self, start):
        try:
            self.logging.info(f'Seleccionando hora de inicio {start}')
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="book--time-picker-start"]'))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[contains(text(), "{start}")]'))).click()
        except Exception as e:
            self.logging.error(f'Error en select_hora_inicio: {e}')
            self._captura_pantalla("select_hora_inicio_error")
            raise
    
    def select_hora_fin(self, end):
        try:
            self.logging.info(f'Seleccionando hora de fin {end}')
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="book--time-picker-end"]'))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[contains(text(), "{end}")]'))).click()
        except Exception as e:
            self.logging.error(f'Error en select_hora_fin: {e}')
            self._captura_pantalla("select_hora_fin_error")
            raise

    def unselect_dia_completo(self):
        try:
            self.logging.info("Desactivando 'Todo el dia'")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="book--switch-full-day"]'))).click()
        except Exception as e:
            self.logging.error(f'Error en unselect_dia_completo: {e}')
            self._captura_pantalla("unselect_dia_completo_error")
            raise

    def reload_boton_reservar(self):
        try:
            self.logging.info("Recargando boton de reservar")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="navigation--book--item"]'))).click()
        except Exception as e:
            self.logging.error(f'Error en reload_boton_reservar: {e}')
            self._captura_pantalla("reload_boton_reservar_error")
            raise

    def confirm_reserva(self):
        try:
            self.logging.info("Confirmando reserva")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Quick book")]'))).click()
        except Exception as e:
            self.logging.error(f'Error en confirm_reserva: {e}')
            self._captura_pantalla("confirm_reserva_error")
            raise
    
    def get_confirm_reserva(self):
        try:
            self.logging.info("Obteniendo mensaje de confirmacion")

            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Booked")]')))
            return True
        except TimeoutException:
            self.logging.info("No se encontró texto 'Booked'")
            return False
        except Exception as e:
            self.logging.error(f'Error en get_confirm_reserva: {e}')
            self._captura_pantalla("get_confirm_reserva_error")
            raise