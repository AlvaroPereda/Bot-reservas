# Bot de reservas Deskbird

Bot en Selenium que automatiza las reservas de sitios de trabajo y parking en [deskbird.com](https://app.deskbird.com). Reserva los huecos configurados con N días de antelación, saltándose los fines de semana.

## Requisitos previos

- Python 3.10+
- Haber iniciado sesión en deskbird

## Instalación

1. Crear un entorno virtual:

   ```bash
   python -m venv venv
   ```

3. Activar el entorno virtual (bash en Windows):

   ```bash
   source venv/Scripts/activate
   ```

4. Instalar las dependencias desde `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   El único paquete necesario es `selenium==4.41.0`.

## Configuración

Toda la configuración está en `settings.py`:

- `RESERVAS` — lista de reservas a realizar (edificio, planta, hora de inicio/fin y días de antelación).
- `HEADLESS` — `False` para ver el navegador mientras se ejecuta.
- `TIMEOUT` — segundos de espera máxima para los elementos.
- `LOGGING_LEVEL` — `DEBUG`, `INFO`, `ERROR` o `CRITICAL`.


## Ejecución

Con el entorno virtual activado:

```bash
python main.py
```

## Depuración

Si una reserva falla, se guarda una captura de pantalla en `capturas/` con el nombre del paso que ha fallado.

## Estructura

- `main.py` — punto de entrada.
- `bot.py` — configuración del driver, lógica de fechas y bucle de reservas.
- `reservas_page.py` — Page Object con toda la interacción con la UI de deskbird.
- `settings.py` — configuración.
- `memoria.md` — documentación del mini-TFG.