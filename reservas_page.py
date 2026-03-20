from selenium.webdriver.support.ui import WebDriverWait

class ReservasPage:

    def __init__(self, driver, timeout):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    