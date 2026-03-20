from dataclasses import dataclass

@dataclass
class ReservaConfig:
    edificio: str
    planta: str
    hora_inicio: int
    hora_fin: int
    dias_anticipacion: int

RESERVAS = [
    ReservaConfig(
        edificio="Parking",
        planta="Sótano 4",
        hora_inicio=33, # 8:00
        hora_fin=61, # 15:00
        dias_anticipacion=3
    ),
    ReservaConfig(
        edificio="Edificio C",
        planta="Planta 4",
        hora_inicio=5, # 8:00
        hora_fin=33, # 15:00
        dias_anticipacion=7
    )
]

URL = "https://app.deskbird.com/planning/calendar"
HEADLESS = True
TIMEOUT = 15
LOGGING_LEVEL = "INFO"  # DEBUG, INFO, ERROR, CRITICAL
MESES = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
