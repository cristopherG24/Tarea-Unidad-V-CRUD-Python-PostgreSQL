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
def mostrar_clientes():
    cursor.execute("SELECT id_cliente, nombre, ciudad FROM public.clientes ORDER BY id_cliente")
    print("Clientes en la base de datos:")
    for fila in cursor.fetchall():
        print(fila)
    print("-" * 45)

mostrar_clientes()
print("Borrar un Cliente")
id_borrar = input("Ingresa el id del cliente a borrar: ")
cursor.execute("DELETE FROM public.clientes WHERE id_cliente = %s", (id_borrar,))
conexion.commit()
mostrar_clientes()
cursor.close()
conexion.close()
print("Conexion cerrada")
