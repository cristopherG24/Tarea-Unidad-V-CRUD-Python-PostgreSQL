# Tarea Unidad V - CRUD con Python y PostgreSQL

Proyecto académico de operaciones CRUD sobre la base de datos PostgreSQL `comercio`.

## Tecnologías
Python 3, PostgreSQL, psycopg2, Visual Studio Code y pgAdmin 4.

## Archivos
- Clientes: `Clientes.py`, `ConsultarCliente.py`, `BorrarCliente.py`
- Productos: `InsertarProducto.py`, `ConsultarProducto.py`, `ModificarProducto.py`, `BorrarProducto.py`
- Pedidos: `InsertarPedido.py`, `ConsultarPedido.py`, `ModificarPedido.py`, `BorrarPedido.py`
- Conexión: `conexion.py`

## Preparación
1. Crear una base de datos PostgreSQL llamada `comercio` con tablas `clientes`, `productos` y `pedidos`.
2. Instalar dependencias: `pip install -r requirements.txt`.
3. En PowerShell, definir la contraseña: `$env:DB_PASSWORD = Read-Host "Contraseña de PostgreSQL"`.
4. Ejecutar, por ejemplo: `python ConsultarProducto.py`.

Los scripts usan localhost:5432, usuario postgres y base de datos comercio. Las operaciones de modificación y borrado alteran los datos. Las capturas de ejecución se incluyen en el documento Word de entrega.