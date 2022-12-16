# Water meter integration for Aguas de Valencia 
Configuration to integrate your Aguas de Valencia water consumption in Home Assistant.

## Steps for configuration
- Paste the code of the `configuration.yaml` file in your Home Assistant configuration file.
- Replace `YOURACCOUNT@EMAIL.COM`and `YOURPASSWORD` values with your Aguas de Valencia's web credentials (you must have an account previously).
- Check config and restart Home Assistant.
- If everything went OK, after a couple of hours you shuld be able to add the new `sensor.contador_aguas_de_valencia` to the Energy Panel

## Known issues
- The value is updated each 24 hours, because I'm only able to get the last value and they update in batches of 24 hours. I'm trying to save all the values with it's corresponding datetime in the sensor, but still work in progress.
- The `scan_interval` is very frequent (1 hour) compared to the value updating time (24 hours), I don't know if this can make the user to be banned.

# ESPAÑOL - SPANISH
Configuracion de Home Assistant para integrar la lectura del consumo de agua desde Aguas de Valencia.

## Pasos para la configuración
- Pega el código del archivo `configuration.yaml` en el archivo de configuración de tu Home Assistant.
- Sustituye los valores de `YOURACCOUNT@EMAIL.COM`y `YOURPASSWORD` con tus credenciales de la web de Aguas de Valencia (debes tener una cuenta previamente).
- Comprueba la configuración y reinicia Home Assistant.
- Si todo ha ido bien, en un par de horas deberías poder añadir el nuevo `sensor.contador_aguas_de_valencia` al Panel de Energía

## Problemas conocidos
- El valor se actualiza cada 24 horas, porque ahora mismo solo soy capaz de extraer el último valor y ellos actualizan en lotes de 24 horas. Estoy intentando guardar todos los valores con su correspondiente fecha y hora en el sensor, pero todavía estoy trabajándolo
- El tiempo de `scan_interval` es muy frecuente (1 hora) comparado con el tiempo de actualización del valor (24 horas), desconozco si esto puede hacer que bloqueen el usuario.
