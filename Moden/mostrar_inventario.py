from ..Servicios.inventario import productos

def mostrar_inventario():
    if len(productos) == 0:
        print("No hay productos en el inventario.")
    else:
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
