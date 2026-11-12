import os
import psycopg2

conexion = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='comercio',
    user='postgres',
    password='5761039'
)
cursor = conexion.cursor()
print("Conexion exitosa a la base de datos")
print("-" * 45)
def mostrar_pedidos():
    cursor.execute("SELECT id_pedido, id_cliente, id_producto, cantidad, fecha FROM public.pedidos ORDER BY id_pedido")
    print("PEDIDOS EN LA BASE DE DATOS")
    pedidos = cursor.fetchall()
    for pedido in pedidos:
        print(pedido)
    if len(pedidos) == 0:
        print("No hay pedidos registrados")
    print("-" * 45)

mostrar_pedidos()
print("BORRAR UN PEDIDO")
id_borrar = int(input("Ingresa el ID del pedido a borrar: "))
cursor.execute("DELETE FROM public.pedidos WHERE id_pedido = %s", (id_borrar,))
filas_eliminadas = cursor.rowcount
conexion.commit()
if filas_eliminadas > 0:
    print("Pedido eliminado correctamente")
else:
    print("No se encontro un pedido con ese ID")
print("-" * 45)
print("PEDIDOS DESPUES DE ELIMINAR")
mostrar_pedidos()
cursor.close()
conexion.close()
print("Conexion cerrada")
