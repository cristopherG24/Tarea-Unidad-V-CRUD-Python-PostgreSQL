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
print("-" * 45)
clientes_nuevos = [
    ("Jose Duarte", "jose@mail.com", "Lambare"),
    ("Sara Nunez", "sara@mail.com", "Villa Elisa"),
    ("Luis Benitez", "luisb@mail.com", "Capiata"),
]
cursor.executemany(
    "INSERT INTO clientes (nombre, email, ciudad) VALUES (%s, %s, %s)",
    clientes_nuevos
)
conexion.commit()
print(f"{cursor.rowcount} clientes insertados de una sola vez")
cursor.close()
conexion.close()
print("Conexion cerrada")
