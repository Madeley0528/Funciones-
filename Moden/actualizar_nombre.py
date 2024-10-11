from ..Servicios.inventario import productos

def actualizar_nombre():
    nombre = input("Nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            nuevo_nombre = input("Nuevo nombre: ")
            producto['nombre'] = nuevo_nombre
            print("Nombre actualizado.")
            return
    print("Producto que no se ha  encontrado.")
    return
print("Producto no encontrado.")
