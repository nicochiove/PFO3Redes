import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="tareasdb",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS tareas (
    id SERIAL PRIMARY KEY,
    descripcion TEXT NOT NULL,
    resultado TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()

cur.close()
conn.close()

print("Base de datos inicializada correctamente")