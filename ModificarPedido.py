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
print("PEDIDOS ANTES DE MODIFICAR")
for fila in cursor.fetchall():
    print(fila)
print("-" * 45)
id_modificar = int(input("Ingresa el ID del pedido a modificar: "))
nueva_cantidad = int(input("Ingresa la nueva cantidad del pedido: "))
cursor.execute("UPDATE public.pedidos SET cantidad = %s WHERE id_pedido = %s", (nueva_cantidad, id_modificar))
filas_modificadas = cursor.rowcount
conexion.commit()
if filas_modificadas > 0:
    print("Pedido actualizado correctamente")
else:
    print("No se encontro un pedido con ese ID")
print("-" * 45)
cursor.execute("SELECT id_pedido, id_cliente, id_producto, cantidad, fecha FROM public.pedidos ORDER BY id_pedido")
print("PEDIDOS DESPUES DE MODIFICAR")
for fila in cursor.fetchall():
    print(fila)
print("-" * 45)
cursor.close()
conexion.close()
print("Conexion cerrada")
