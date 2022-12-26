# Código generado con ayuda de ChatGPT

from datetime import datetime, timedelta

import json
import requests


login_data = {
    "login": "YOURACCOUNT@EMAIL.COM",
    "pass": "YOURPASSWORD",
    "remember": "true",
    "suministro": "",
}

URL = "https://www.aguasdevalencia.es/VirtualOffice"

session = requests.Session()
response = session.post(f"{URL}/action_Login", data=login_data)

if response.ok:
    # Obtener fecha y hora actuales, asignarlos a variable end_date y convertir a formato dd/mm/yyyy
    now = datetime.now()
    end_date = now.date()
    end_date = end_date.strftime("%d/%m/%Y")
    # Restar 7 días a fecha actual, asignar a variable start_date y convertirlo a formato dd/mm/yyyy
    last_week = now - timedelta(days=7)
    start_date = last_week.date()
    start_date = start_date.strftime("%d/%m/%Y")
    # Obtener datos de lectura horaria entre fechas
    request_dates = f"start={start_date}&end={end_date}"
    response = session.get(f"{URL}/Secure/action_getDatosLecturaHorariaEntreFechas?{request_dates}")

    if response.ok:
        json_data = response.json()
        # Procesar datos aquí...
        data = json_data["data"]["datasets"][0]["data"][-1:][0]
        title = data["title"] # Lectura anterior
        y = data["y"] # Consumo actual ultima hora registrada
        # Reemplazar la coma por un punto y convertir a float la lectura anterior
        title = title.replace(",", ".")
        title = float(title)
        # Dividir consumo última hora por 1000 (cambio de unidades) y sumar a la lectura anterior
        result = title + y / 1000
        print(result)
    else:
        print(f"Error al obtener datos de lectura horaria: {response.status_code}")
else:
    print(f"Error al iniciar sesión: {response.status_code}")
