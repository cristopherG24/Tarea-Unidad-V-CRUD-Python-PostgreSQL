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
def mostrar_productos():
    cursor.execute("SELECT id_producto, nombre, precio, stock FROM public.productos ORDER BY id_producto")
    print("PRODUCTOS EN LA BASE DE DATOS")
    for fila in cursor.fetchall():
        print(fila)
    print("-" * 45)

mostrar_productos()
print("BORRAR UN PRODUCTO")
id_borrar = int(input("Ingresa el ID del producto a borrar: "))
cursor.execute("DELETE FROM public.productos WHERE id_producto = %s", (id_borrar,))
filas_borradas = cursor.rowcount
conexion.commit()
if filas_borradas > 0:
    print("Producto eliminado correctamente")
else:
    print("No se encontro un producto con ese ID")
print("-" * 45)
print("PRODUCTOS DESPUES DE ELIMINAR")
mostrar_productos()
cursor.close()
conexion.close()
print("Conexion cerrada")
