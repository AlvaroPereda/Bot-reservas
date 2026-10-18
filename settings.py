import os
from dataclasses import dataclass
from datetime import date
from typing import Final

from dotenv import load_dotenv

load_dotenv()

CHROMIUM_BINARY: str = os.getenv("CHROMIUM_BINARY", "/usr/bin/chromium")
CHROMEDRIVER_PATH: str = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")
CHROME_USER_DATA_DIR: str | None = os.getenv("CHROME_USER_DATA_DIR")
CHROME_PROFILE: str = os.getenv("CHROME_PROFILE", "Default")


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

URL: str = "https://app.deskbird.com/planning/calendar"
HEADLESS: bool = True
TIMEOUT: int = 15
LOGGING_LEVEL: str = "INFO"  # DEBUG, INFO, ERROR, CRITICAL
MESES: Final = [
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
HOME: Final = [1, 4]  # Dias de teletrabajo (0=Lunes, 1=Martes, ..., 4=Viernes)
VACACIONES: Final = [
    # date(2026, 12, 24),
    # date(2026, 12, 25),
]  # Dias de vacaciones (se salta la reserva)
