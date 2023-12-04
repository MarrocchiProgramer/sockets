import socket

def main():
  # Creamos un socket
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Conectamos al servidor
  client_socket.connect(("localhost", 8080))

  # Iniciamos un bucle
  while True:

    # Recibimos la respuesta del servidor
    respuesta = client_socket.recv(1024).decode()

    # Si la respuesta es "Conexión iniciada", entonces es el mensaje de bienvenida
    if respuesta == "Conexión iniciada":
      # El servidor ya nos ha enviado el número secreto
      # No necesitamos introducir una respuesta
      pass
    else:
      # La respuesta es una respuesta del juego
      # Introducimos la respuesta en el juego
      print(respuesta)
      respuesta = input("Introduce tu respuesta: ")
      client_socket.send(respuesta.encode())

  # Cerramos la conexión
  client_socket.close()

if __name__ == "__main__":
  main()
