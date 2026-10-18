import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

CHROMIUM_BINARY = os.getenv("CHROMIUM_BINARY", "/usr/bin/chromium")
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")
CHROME_USER_DATA_DIR = os.getenv("CHROME_USER_DATA_DIR")
CHROME_PROFILE = os.getenv("CHROME_PROFILE", "Default")


@dataclass
class ReservaConfig:
    edificio: str
    planta: str
    hora_inicio: str
    hora_fin: str
    dias_anticipacion: int


RESERVAS = [
    ReservaConfig(
        edificio="Parking",
        planta="Sótano 4",
        hora_inicio="07:30",
        hora_fin="16:00",
        dias_anticipacion=3,
    ),
    ReservaConfig(
        edificio="Edificio C",
        planta="Planta 4",
        hora_inicio="07:30",
        hora_fin="16:00",
        dias_anticipacion=7,
    ),
]

URL = "https://app.deskbird.com/planning/calendar"
HEADLESS = True
TIMEOUT = 15
LOGGING_LEVEL = "INFO"  # DEBUG, INFO, ERROR, CRITICAL
MESES = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
HOME = [1, 4]  # Dias de telebrajo (0=Lunes, 1=Martes, ..., 4=Viernes)
