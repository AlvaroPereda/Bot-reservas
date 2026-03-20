from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ReservasPage:

    def __init__(self, driver, timeout, logging):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logging = logging

    def open_panel_reserva(self):
        self.logging.info("Abriendo menu de reservas")
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="navigation--book--item"]'))).click()

    def open_calendario(self):
        self.logging.info("Abriendo calendario")
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "calendar-icon-container"))).click()
    
    def select_edificio(self, edificio):
        self.logging.info(f'Seleccionado edificio {edificio}')
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="book--office-selector"]'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[aria-posinset="{edificio}"]'))).click()
    
    def select_planta(self, planta):
        self.logging.info(f'Seleccionado planta {planta}')
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="book--floor-selector"]'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[aria-posinset="{planta}"]'))).click()

    def select_mes(self, mes):
        self.logging.info(f'Ajustando mes a {mes}')
        while True:
            mes_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="Choose Month"]')))
            mes_actual = mes_element.text

            if mes == mes_actual:
                break

            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Next Month"]'))).click()
    
    def select_dia(self, fecha):
        testid = fecha.strftime("%Y-%m-%d")
        self.logging.info(f'Seleccionando dia {testid}')
        dia_element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[data-testid="{testid}"]')))
        self.driver.execute_script("arguments[0].click();", dia_element)

    def select_hora_inicio(self, start):
        self.logging.info(f'Seleccionando hora de inicio {start}')
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="book--time-picker-start"]'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[aria-posinset="{start}"]'))).click()
    
    def select_hora_fin(self, end):
        self.logging.info(f'Seleccionando hora de fin {end}')
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="book--time-picker-end"]'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[aria-posinset="{end}"]'))).click()

    def unselect_dia_completo(self):
        self.logging.info("Desactivando 'Todo el dia'")
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="book--switch-full-day"]'))).click()

    def reload_boton_reservar(self):
        self.logging.info("Recargando boton de reservar")
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="navigation--book--item"]'))).click()

    def confirm_reserva(self):
        self.logging.info("Confirmando reserva")
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="book--confirm-button"]'))).click()