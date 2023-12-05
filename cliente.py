# Cliente
import socket
def main():
    host = "localhost"
    port = 8080

    # Creamos el socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Nos conectamos al servidor
    sock.connect((host, port))

    # Recibimos la contraseña del servidor
    contraseña = sock.recv(1024).decode()

    # Comenzamos el juego
    intentos = 1

    
    respuesta = eval(input("Adivina un número: "))

    # Mientras no hayamos adivinado la contraseña o no hayamos agotado los intentos
    while contraseña != respuesta and intentos <= 15:

        # Solicitamos la respuesta del usuario
        respuesta = input("Adivina un número: ")

        # Enviamos la respuesta al servidor
        sock.sendall(respuesta.encode())

        # Recibimos el mensaje del servidor
        mensaje = sock.recv(1024).decode()

        # Imprimimos el mensaje del servidor
        print(mensaje)

        # Incrementamos el número de intentos
        intentos += 1

    # Si adivinamos la contraseña
    if contraseña == respuesta:

        # Imprimimos un mensaje de victoria
        print("Has ganado!")

    # Si agotamos los intentos
    else:

        # Imprimimos un mensaje de derrota
        print("Has perdido!")

    sock.close()

if __name__ == "__main__":
    main()
