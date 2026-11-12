import os
import psycopg2

conexion = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='comercio',
    user='postgres',
    password='********'
)

cursor = conexion.cursor()
print("Conexion exitosa a la base de datos")
cursor.execute("SELECT id_cliente, nombre, email, ciudad, fecha_alta FROM public.clientes ORDER BY id_cliente")
for fila in cursor.fetchall():
    print(fila)
cursor.close()
conexion.close()
print("Conexion cerrada")
