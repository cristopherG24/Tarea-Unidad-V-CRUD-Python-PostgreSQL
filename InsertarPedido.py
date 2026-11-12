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
id_cliente = int(input("Ingresa el ID del cliente: "))
id_producto = int(input("Ingresa el ID del producto: "))
cantidad = int(input("Ingresa la cantidad del pedido: "))
cursor.execute(
    "INSERT INTO public.pedidos (id_cliente, id_producto, cantidad) VALUES (%s, %s, %s) RETURNING id_pedido",
    (id_cliente, id_producto, cantidad)
)
id_pedido = cursor.fetchone()[0]
conexion.commit()
print("-" * 45)
print("Pedido insertado correctamente")
print("ID del pedido:", id_pedido)
print("ID del cliente:", id_cliente)
print("ID del producto:", id_producto)
print("Cantidad:", cantidad)
cursor.close()
conexion.close()
print("Conexion cerrada")
