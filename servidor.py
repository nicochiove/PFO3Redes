import socket
import threading

from cola_tareas import cola_tareas
from database import guardar_tarea
from worker import worker

HOST = "127.0.0.1"
PORT = 5001

NUM_WORKERS = 4


def iniciar_workers():

    for i in range(NUM_WORKERS):

        hilo = threading.Thread(
            target=worker,
            daemon=True,
            name=f"Worker-{i+1}"
        )

        hilo.start()


def manejar_cliente(conn, addr):

    print(f"Cliente conectado: {addr}")

    try:

        tarea = conn.recv(1024).decode()

        tarea_id = guardar_tarea(tarea)

        print(
            f"Tarea {tarea_id} recibida: {tarea}"
        )

        cola_tareas.put(
            (tarea_id, tarea, conn)
        )

    except Exception as e:

        print(e)

        conn.close()


def iniciar_servidor():

    iniciar_workers()

    servidor = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    servidor.bind((HOST, PORT))

    servidor.listen()

    print(
        f"Servidor escuchando en "
        f"{HOST}:{PORT}"
    )

    while True:

        conn, addr = servidor.accept()

        threading.Thread(
            target=manejar_cliente,
            args=(conn, addr),
            daemon=True
        ).start()


if __name__ == "__main__":
    iniciar_servidor()