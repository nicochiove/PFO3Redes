from cola_tareas import cola_tareas
from database import actualizar_resultado
import threading
import time


def procesar_tarea(texto):
    time.sleep(2)

    return texto.upper()


def worker():

    while True:

        tarea_id, descripcion, conexion_cliente = cola_tareas.get()

        print(
            f"[{threading.current_thread().name}] "
            f"Procesando tarea {tarea_id}"
        )

        resultado = procesar_tarea(descripcion)

        actualizar_resultado(tarea_id, resultado)

        conexion_cliente.send(
            f"Resultado: {resultado}".encode()
        )

        conexion_cliente.close()

        cola_tareas.task_done()