from decimal import Decimal
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
print("PRODUCTOS ANTES DE MODIFICAR")
for fila in cursor.fetchall():
    print(fila)
print("-" * 45)
id_modificar = int(input("Ingresa el ID del producto a modificar: "))
nuevo_precio = Decimal(input("Ingresa el nuevo precio del producto: "))
cursor.execute("UPDATE public.productos SET precio = %s WHERE id_producto = %s", (nuevo_precio, id_modificar))
filas_modificadas = cursor.rowcount
conexion.commit()
if filas_modificadas > 0:
    print("Producto actualizado correctamente")
else:
    print("No se encontro un producto con ese ID")
print("-" * 45)
cursor.execute("SELECT id_producto, nombre, precio, stock FROM public.productos ORDER BY id_producto")
print("PRODUCTOS DESPUES DE MODIFICAR")
for fila in cursor.fetchall():
    print(fila)
print("-" * 45)
cursor.close()
conexion.close()
print("Conexion cerrada")
