from ..Servicios.inventario import productos

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            print("Producto eliminado.")
            return
    print("Producto que se ha  encontrado.")
