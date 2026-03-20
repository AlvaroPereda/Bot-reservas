from dataclasses import dataclass

@dataclass
class ReservaConfig:
    edificio: int
    planta: int
    hora_inicio: int
    hora_fin: int
    dias_anticipacion: int

RESERVAS = [
    ReservaConfig(
        edificio=4, # Parking
        planta=5, # Sotano 4
        hora_inicio=33, # 8:00
        hora_fin=61, # 15:00
        dias_anticipacion=3
    ),
    ReservaConfig(
        edificio=3, # Edificio C
        planta=4, # Planta 4
        hora_inicio=5, # 8:00
        hora_fin=33, # 15:00
        dias_anticipacion=7
    )
]

URL = "https://app.deskbird.com/planning/calendar"
HEADLESS = False
TIMEOUT = 15
LOGGING_LEVEL = "INFO"  # DEBUG, INFO, ERROR, CRITICAL
MESES = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
