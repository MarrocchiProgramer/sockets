import socket
import random

def main():
  # Creamos un socket
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Imprimimos un mensaje
  print("Servidor iniciado")

  # Bindeamos el socket a una dirección y puerto
  server_socket.bind(('', 8080))

  # Escuchamos por conexiones entrantes
  server_socket.listen(5)

  # Aceptamos una conexión entrante
  connection, address = server_socket.accept()

  # Elegimos un número al azar
  numero_secreto = random.randint(1, 10)

  # Enviamos un mensaje de bienvenida
  connection.send("¿Cuál crees que elegí?".encode())

  # Iniciamos un bucle
  while True:

    # Recibimos la respuesta del cliente
    respuesta = connection.recv(1024).decode()

    # Si la respuesta es correcta
    if respuesta == str(numero_secreto):
      # Enviamos un mensaje de victoria
      connection.send("Has ganado!".encode())
      break
    else:
      # Enviamos un mensaje de derrota
      connection.send("Respuesta incorrecta, elige otro número".encode())

  # Cerramos la conexión
  connection.close()

if __name__ == "__main__":
  main()
