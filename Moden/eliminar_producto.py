
# Como se elimina un producto 
def eliminar_producto(nombre):
    for producto in inventario:
        if producto["nombre"] == nombre:
            inventario.remove(producto)
            print(f"Producto {nombre} eliminado exitosamente.")
            return
    print("Producto no encontrado.")