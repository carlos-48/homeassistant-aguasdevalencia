# Código generado con ayuda de ChatGPT

import json
import requests

login_data = {
    "login": "YOURACCOUNT@EMAIL.COM",
    "pass": "YOURPASSWORD",
    "remember": "true",
    "suministro": "",
}

url = "https://www.aguasdevalencia.es/VirtualOffice"

session = requests.Session()
response = session.post(f"{url}/action_Login", data=login_data)

if response.ok:
    # Obtener datos de lectura horaria entre fechas
    start_date = "01/01/2021"  # Fecha de inicio, formato dd/mm/yyyy
    end_date = "01/01/2022"  # Fecha final, formato dd/mm/yyyy
    request_dates = f"start={start_date}&end={end_date}"
    response = session.get(f"{url}/Secure/action_getDatosLecturaHorariaEntreFechas?{request_dates}")

    if response.ok:
        data = response.json()
        # Procesar datos aquí...
        data = value_json["data"]["datasets"][0]["data"][-1:][0]
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
