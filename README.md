# multiscrape-ha-aguas-de-valencia
Configuration for the Home Assistant `multiscrape` custom-component for reading the water consumption from Aguas de Valencia.

## Steps for configuration
- Install [multiscrape](https://github.com/danieldotnl/ha-multiscrape) custom-component to your Home Assistant, via HACS Store or manually.
- Paste the code of the `configuration.yaml` file in your Home Assistant configuration file.
- Paste the code of the `secrets.yaml` file in your Home Assistant secrets file, and replace `aguas_de_valencia_session_login`and `aguas_de_valencia_session_password` values with your Aguas de Valencia's web credentials (you must have an account previously).
- Go to the Aguas de Valencia [Virtual Office](https://www.aguasdevalencia.es/VirtualOffice) and log in with your credentials (you must have an account previously).
- Open the Developers Tools of your browser (in Chrome Desktop, `Ctrl`+`Shift`+`I`). 
- Then go to Aplication in the top menu.
- Go to Storage>Cookies in the left menu, and click on `https://www.aguasdevalencia.es`.
- On the rigth table, copy the value of the `x_SessionId` cookie (it would be an 24 character string).
- Go again to your secrets file, and paste that value in `aguas_de_valencia_session_id`.
- Check config and restart Home Assistant.

## Known issues (don't know how to solve it)
- The `x_SessionId` cookie can expire and you may log in again and copy the new value. Maybe there is a way to automate this, but I don't know how to do it.
- The `scan_interval` is very agresive, I'm using this to try keeping the session alive, but I don't know if this can make the user to be banned.

# ESPAÑOL - SPANISH
Configuracion de Home Assistant para el custom-component `multiscrape` para la lectrua del consumo de agua desde Aguas de Valencia.

## Pasos para la configuración
- Instalar el custom-component [multiscrape](https://github.com/danieldotnl/ha-multiscrape) en tu Home Assistant, via la tienda HACS Store o manualmente.
- Pega el código del archivo `configuration.yaml` en el archivo de configuración de tu Home Assistant.
- Pega el código del archivo `secrets.yaml` en el archivo de secretos de tu Home Assistant, y sustituye los valores de `aguas_de_valencia_session_login`y `aguas_de_valencia_session_password` con tus credenciales de la web de Aguas de Valencia (debes tener una cuenta previamente).
- Ve a la [Oficina Virtual](https://www.aguasdevalencia.es/VirtualOffice) de Aguas de Valencia e inicia sesión con tus credenciales (debes tener una cuenta previamente).
- Abre las Herramientas para Desarrolladores de tu navegador (en Chrome para Escritorio, `Ctrl`+`Shift`+`I`). 
- Luego ve a Aplicación en el menú superior.
- Ve a Almacenamiento>Cookies en el menú izquierdo, y pulsa en `https://www.aguasdevalencia.es`.
- En la tabla derecha, copia el valor de la cookie `x_SessionId` (debe ser una cadena de 24 caracteres).
- Vuelve a tu archivo de secretos, y pega ese valor en `aguas_de_valencia_session_id`.
- Comprueba la configuración y reinicia Home Assistant.

## Prblemas conocidos (no sé cómo solventarlos)
- La cookie `x_SessionId` puede caducar y debes iniciar sesión de nuevo y copiar el nuevo valor. Tal vez hay una forma de automatizar esto, pero no sé cómo hacerlo.
- El tiempo de `scan_interval` es muy agresivo, estoy usando esto para tratar de mantener activa la sesión, pero desconozco si esto puede hacer que bloqueen el usuario.
