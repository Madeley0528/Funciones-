from..Servicios.inventario import productos

def actualizar_cantidad():
    nombre = input("Nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            nueva_cantidad = input("Nueva cantidad: ")
            while not nueva_cantidad.isdigit():
                nueva_cantidad = input("Introduce algo válido: ")
            producto['cantidad'] = int(nueva_cantidad)
            print("Cantidad actualizada.")
            return
    print("Producto que no se encuentra ")

   


