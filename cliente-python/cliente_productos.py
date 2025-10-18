import requests

BASE_URL = "http://localhost:8080/api/productos"

# ===============================================================
# Funciones para consumir el servicio web
# ===============================================================

def obtener_productos():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        productos = response.json()
        if productos:
            print("\nLista de productos:")
            for p in productos:
                print(f"ID: {p['id']} | {p['nombre']} | Marca: {p['marca']} | Precio: {p['precio']} | Stock: {p['stock']} | Especificaciones: {p['especificaciones']}")
        else:
            print("No hay productos registrados.")
    else:
        print("Error al obtener productos:", response.status_code)

def crear_producto():
    print("\nCrear nuevo producto")
    nombre = input("Nombre: ")
    marca = input("Marca: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))
    especificaciones = input("Especificaciones técnicas: ")

    producto = {
        "nombre": nombre,
        "marca": marca,
        "precio": precio,
        "stock": stock,
        "especificaciones": especificaciones
    }

    response = requests.post(BASE_URL, json=producto)
    if response.status_code in (200, 201):
        print("Producto creado correctamente:", response.json())
    else:
        print("Error al crear producto:", response.status_code, response.text)

def obtener_producto_por_id():
    id_producto = input("\nIngrese el ID del producto: ")
    response = requests.get(f"{BASE_URL}/{id_producto}")
    if response.status_code == 200:
        print("Detalles del producto:", response.json())
    else:
        print("Producto no encontrado.")

def actualizar_producto():
    id_producto = input("\nIngrese el ID del producto a actualizar: ")
    nombre = input("Nuevo nombre: ")
    marca = input("Nueva marca: ")
    precio = float(input("Nuevo precio: "))
    stock = int(input("Nuevo stock: "))
    especificaciones = input("Nuevas especificaciones: ")

    producto_actualizado = {
        "nombre": nombre,
        "marca": marca,
        "precio": precio,
        "stock": stock,
        "especificaciones": especificaciones
    }

    response = requests.put(f"{BASE_URL}/{id_producto}", json=producto_actualizado)
    if response.status_code == 200:
        print("Producto actualizado:", response.json())
    else:
        print("Error al actualizar producto:", response.status_code)

def eliminar_producto():
    id_producto = input("\nIngrese el ID del producto a eliminar: ")
    response = requests.delete(f"{BASE_URL}/{id_producto}")
    if response.status_code == 204:
        print("Producto eliminado correctamente.")
    else:
        print("Error al eliminar producto:", response.status_code)

def buscar_por_marca():
    marca = input("\nIngrese la marca a buscar: ")
    response = requests.get(f"{BASE_URL}/buscar/{marca}")
    if response.status_code == 200:
        productos = response.json()
        if productos:
            print(f"\nProductos de la marca '{marca}':")
            for p in productos:
                print(f"ID: {p['id']} | {p['nombre']} | Precio: {p['precio']} | Stock: {p['stock']} | Especificaciones: {p['especificaciones']}")
        else:
            print(f"No se encontraron productos de la marca {marca}.")
    else:
        print("Error al buscar por marca:", response.status_code)

# ===============================================================
# Menú interactivo
# ===============================================================

def menu():
    while True:
        print("\n========== CLIENTE PYTHON - TECNO CMD ==========")
        print("1. Ver todos los productos")
        print("2. Crear un producto nuevo")
        print("3. Buscar producto por ID")
        print("4. Buscar productos por marca")
        print("5. Actualizar producto")
        print("6. Eliminar producto")
        print("0. Salir")
        print("===================================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            obtener_productos()
        elif opcion == "2":
            crear_producto()
        elif opcion == "3":
            obtener_producto_por_id()
        elif opcion == "4":
            buscar_por_marca()
        elif opcion == "5":
            actualizar_producto()
        elif opcion == "6":
            eliminar_producto()
        elif opcion == "0":
            print("Saliendo del cliente...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# ===============================================================
# Ejecutar
# ===============================================================
if __name__ == "__main__":
    menu()
