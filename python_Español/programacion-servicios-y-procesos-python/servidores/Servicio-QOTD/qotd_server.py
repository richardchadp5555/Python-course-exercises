# servicio-QOTD
# Este ejercicio tiene como objetivo comprender conceptos como la creación y configuración de sockets en Python, 
# la comunicación cliente-servidor y pruebas de servicios con herramientas como Telnet.
# Lenguaje: Python
# Autor: Richard Chadwick Plaza

import socket
import random

# Frases para el servicio "Cita del día"
quotes = [
    # Einstein
    "La vida es como andar en bicicleta. Para mantener el equilibrio debes seguir moviéndote. - Albert Einstein",
    "No todo lo que puede ser contado cuenta, y no todo lo que cuenta puede ser contado. - Albert Einstein",
    "La imaginación es más importante que el conocimiento. - Albert Einstein",

    # Oppenheimer
    "En algún momento, se convierte en un deber moral de los hombres el asumir el riesgo de sus actos. - J. Robert Oppenheimer",
    "Ahora me he convertido en la muerte, el destructor de mundos. - J. Robert Oppenheimer",

    # Heisenberg
    "Lo que observamos no es la naturaleza misma, sino la naturaleza expuesta a nuestro método de interrogación. - Werner Heisenberg",
    "La realidad es sólo una ilusión, aunque muy persistente. - Werner Heisenberg",

    # Planck
    "Cuando cambias la forma de ver las cosas, las cosas que ves cambian. - Max Planck",
    "La ciencia no puede resolver el último misterio de la naturaleza. Esto se debe a que, en el análisis final, nosotros mismos somos parte del misterio que intentamos resolver. - Max Planck",

    # Nietzsche
    "Sin música, la vida sería un error. - Friedrich Nietzsche",
    "Lo que no me mata, me hace más fuerte. - Friedrich Nietzsche",
    "Cuando miras largo tiempo a un abismo, el abismo también mira dentro de ti. - Friedrich Nietzsche",

    # Shakespeare
    "Ser o no ser, esa es la cuestión. - William Shakespeare",
    "El amor no mira con los ojos, sino con el alma. - William Shakespeare",
    "El destino es el que baraja las cartas, pero nosotros somos los que jugamos. - William Shakespeare"
]

# 1. Crear el socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Enlazar el socket a una dirección y puerto
server_address = ('192.168.10.55', 2017)  # Ponemos nuestra IP privada
server_socket.bind(server_address)

# 3. Poner el socket en modo escucha
server_socket.listen(5)  # Permite hasta cinco conexiones
print(f"Servidor QOTD escuchando en {server_address}")

while True:
    # 4. Aceptar conexiones
    client_socket, client_address = server_socket.accept()
    print(f"Conexión aceptada desde {client_address}")

    # 5. Enviar una frase aleatoria
    quote = random.choice(quotes)
    client_socket.sendall(quote.encode('utf-8'))  # Enviar respuesta

    # 6. Cerrar la conexión
    client_socket.close()
