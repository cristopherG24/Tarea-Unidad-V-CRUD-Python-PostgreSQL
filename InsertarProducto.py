from decimal import Decimal
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
nombre = input("Ingresa el nombre del producto: ")
precio = Decimal(input("Ingresa el precio del producto: "))
stock = int(input("Ingresa la cantidad en stock: "))
cursor.execute(
    "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s) RETURNING id_producto",
    (nombre, precio, stock)
)
id_producto = cursor.fetchone()[0]
conexion.commit()
print("-" * 45)
print("Producto insertado correctamente")
print("ID del producto:", id_producto)
print("Nombre:", nombre)
print("Precio:", precio)
print("Stock:", stock)
cursor.close()
conexion.close()
print("Conexion cerrada")
