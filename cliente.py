import socket

HOST = "127.0.0.1"
PORT = 5001


def enviar_tarea():

    tarea = input(
        "Ingrese descripción de la tarea: "
    )

    cliente = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    cliente.connect(
        (HOST, PORT)
    )

    cliente.send(
        tarea.encode()
    )

    resultado = cliente.recv(1024)

    print(
        resultado.decode()
    )

    cliente.close()


if __name__ == "__main__":
    enviar_tarea()