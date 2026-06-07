import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="tareasdb",
        user="postgres",
        password="postgres"
        )


def guardar_tarea(descripcion):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO tareas(descripcion)
        VALUES(%s)
        RETURNING id
        """,
        (descripcion,)
    )

    tarea_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return tarea_id


def actualizar_resultado(tarea_id, resultado):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE tareas
        SET resultado=%s
        WHERE id=%s
        """,
        (resultado, tarea_id)
    )

    conn.commit()

    cur.close()
    conn.close()