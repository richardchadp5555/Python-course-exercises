# Servicio de QOTD (Quote of the Day) - Ejercicio 1

## Enunciado
Este proyecto implementa un servicio llamado **"Cita del Día"** que funciona en el puerto **2017** de tu equipo. El servicio responde a cada conexión con una frase aleatoria tomada de un conjunto de citas predefinidas. Los clientes pueden conectarse al servidor mediante el protocolo Telnet.

## Requisitos
1. **Crear el servidor:**
   - El servidor debe escuchar en el puerto **2017**.
   - Al recibir una conexión, enviará una frase aleatoria al cliente desde un array predefinido.
   - Después de enviar la frase, cerrará la conexión automáticamente.

2. **Pruebas locales:**
   - Verificar el funcionamiento conectándose desde el mismo equipo mediante el comando `telnet`.

3. **Pruebas desde otro equipo:**
   - Compartir la dirección IP privada y probar el acceso al servidor desde otro dispositivo dentro de la misma red.

4. **Despliegue (opcional):**
   - Desplegar el servidor en un servicio de nube (como Oracle Cloud) abriendo el puerto 2017 para permitir conexiones externas.

## Ejecución
1. Asegúrate de tener Python instalado en tu sistema.
2. Guarda el archivo del servidor como `qotd_server.py`.
3. Ejecuta el servidor con el siguiente comando en tu terminal:
   ```bash
   python qotd_server.py
