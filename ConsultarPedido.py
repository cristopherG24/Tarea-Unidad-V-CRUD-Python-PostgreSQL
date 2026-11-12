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
cursor.execute("SELECT id_pedido, id_cliente, id_producto, cantidad, fecha FROM public.pedidos ORDER BY id_pedido")
print("PEDIDOS EN LA BASE DE DATOS")
print("-" * 45)
pedidos = cursor.fetchall()
for pedido in pedidos:
    print(pedido)
print("-" * 45)
print("Total de pedidos:", len(pedidos))
cursor.close()
conexion.close()
print("Conexion cerrada")
