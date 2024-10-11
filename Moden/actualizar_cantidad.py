# Precios de productos 

# Lista para almacenar los productos
inventario = [

]

# Función para validar que el precio sea positivo
def validar_precio(precio):
    return precio > 0

# Función para agregar un producto al inventario
def agregar_producto(nombre, cantidad, precio):
    if validar_precio(precio):
        producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
        inventario.append(producto)
        print(f"Producto {nombre} agregado exitosamente.")
    else:
        print("El precio debe ser positivo.")

# Función para eliminar un producto del inventario
def eliminar_producto(nombre):
    for producto in inventario:
        if producto["nombre"] == nombre:
            inventario.remove(producto)
            print(f"Producto {nombre} eliminado exitosamente.")
            return
    print("Producto no encontrado.")

# Función para mostrar todo el inventario
def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: Q{producto['precio']}")

# Función para mostrar el valor total del inventario
def mostrar_valor_total():
    total = sum(producto['cantidad'] * producto['precio'] for producto in inventario)
    print(f"El valor total del inventario es: Q{total}")

# Función para actualizar el nombre de un producto
def actualizar_nombre(nombre_actual, nuevo_nombre):
    for producto in inventario:
        if producto["nombre"] == nombre_actual:
            producto["nombre"] = nuevo_nombre
            print(f"Nombre actualizado a {nuevo_nombre}.")
            return
    print("Producto no encontrado.")

# Función para actualizar la cantidad de un producto
def actualizar_cantidad(nombre, nueva_cantidad):
    for producto in inventario:
        if producto["nombre"] == nombre:
            producto["cantidad"] = nueva_cantidad
            print(f"Cantidad de {nombre} actualizada a {nueva_cantidad}.")
            return
    print("Producto no encontrado.")

# Función para actualizar el precio de un producto
def actualizar_precio(nombre, nuevo_precio):
    if validar_precio(nuevo_precio):
        for producto in inventario:
            if producto["nombre"] == nombre:
                producto["precio"] = nuevo_precio
                print(f"Precio de {nombre} actualizado a Q{nuevo_precio}.")
                return
        print("Producto no encontrado.")
   


