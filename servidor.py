import socket
import random

# Servidor

def main():
    host = "localhost"
    port = 8080

    # Creamos el socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Escuchamos conexiones
    sock.bind((host, port))
    sock.listen(1)

    # Aceptamos una conexión
    connection, address = sock.accept()

    # Generamos la contraseña
    contraseña = "".join([str(random.randint(1, 9)) for i in range(5)])

    # Enviamos la contraseña al cliente
    connection.sendall(contraseña.encode())

    # Recibimos la respuesta del cliente
    respuesta = input("Adivina un número: ")

    # Contamos el número de intentos
    intentos = 1

    # Mientras el cliente no adivine la contraseña o no agote los intentos
    while contraseña != respuesta and intentos <= 15:

        # Si el cliente adivinó un número de la contraseña
        if respuesta in contraseña:

            # Le avisamos al cliente que adivinó un número
            connection.sendall("Has adivinado un número!".encode())

            # Contamos el número de números adivinados
            numeros_adivinados = contraseña.count(respuesta)

            # Convertimos el número de números adivinados a una cadena de bytes
            numeros_adivinados_bytes = numeros_adivinados.encode()

            # Enviamos el número de números adivinados al cliente
            connection.sendall(numeros_adivinados_bytes)

        # Si el cliente no adivinó ningún número de la contraseña
        else:

            # Le avisamos al cliente que no adivinó ningún número
            connection.sendall("No has adivinado ningún número!".encode())

        # Recibimos la respuesta del cliente
        respuesta = input("Adivina un número: ")

        # Incrementamos el número de intentos
        intentos += 1

    # Si el cliente agotó los intentos
    if intentos > 15:

        # Le avisamos al cliente que perdió
        connection.sendall("Has perdido!".encode())

    # Cerramos la conexión
    connection.close()

if __name__ == "__main__":
    main()