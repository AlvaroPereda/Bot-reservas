from dataclasses import dataclass

@dataclass
class ReservaConfig:
    edificio: str
    planta: str
    hora_inicio: str
    hora_fin: str
    dias_anticipacion: int

RESERVAS = [
    ReservaConfig (
        edificio="Parking",
        planta="Sótano 4",
        hora_inicio="08:00",
        hora_fin="15:00",
        dias_anticipacion=3
    ),
    ReservaConfig (
        edificio="Edificio C",
        planta="Planta 4",
        hora_inicio="08:00",
        hora_fin="15:00",
        dias_anticipacion=7
    )
]

URL = "https://app.deskbird.com/planning/calendar"
HEADLESS = True
TIMEOUT = 15
LOGGING_LEVEL = "INFO"  # DEBUG, INFO, ERROR, CRITICAL
MESES = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
HOME = [1, 4] # Dias de telebrajo (0=Lunes, 1=Martes, ..., 4=Viernes)
