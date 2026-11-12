import os
import psycopg2

conexion = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='comercio',
    user='postgres',
    password=os.environ['DB_PASSWORD']
)
cursor = conexion.cursor()
print("Conexion exitosa a la base de datos")
print("-" * 45)
cursor.execute("SELECT id_producto, nombre, precio, stock FROM public.productos ORDER BY id_producto")
print("PRODUCTOS EN LA BASE DE DATOS")
print("-" * 45)
productos = cursor.fetchall()
for producto in productos:
    print(producto)
print("-" * 45)
print("Total de productos:", len(productos))
cursor.close()
conexion.close()
print("Conexion cerrada")
