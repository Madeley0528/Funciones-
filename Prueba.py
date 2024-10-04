tareas = [("Estudiar para el examen", "Revisar capítulos 1 a 5", "en progreso"),
("Hacer ejercicio", "Ir al gimnasio por 1 hora", "completada"),
("Llamar al médico", "Solicitar una cita para chequeo", "pendiente"),
("Enviar el informe", "Enviar el informe a mi jefe por correo", "en progreso")]

def mostrar_menu():
    print("--- Menú_mady ---")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")
    print("5. Otras funciones (Estamos programando)")

def agrega_tarea():
    nombre = input("Ingrese un nombre de la tarea: ")
    detalles = input("Ingrese los detalles princiaples  de la tarea: ")
    estado = input("Ingrese el estado de la tarea (en proces, completa, esta_pendiente): ")
    tareas.append((nombre, detalles, estado))
    print(f"Tarea '{nombre}' agregada excelentemente.")

def elimina_tarea():

    print("--- Tareas actuales ---")
    for idx, tarea in enumerate(tareas, start=1):
        print(f"{idx}. {tarea[0]} - {tarea[2]}")

    tarea_di = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
    if 0 <= tarea_di < len(tareas):
        tarea_eliminada = tareas.pop(tarea_di)
        print(f"Tarea '{tarea_eliminada[0]}' eliminada.")
    else:
        print("di de tarea inválido.")

def muestra_tareas():
    if tareas:
        print("--- Tareas ---")
        for tarea in tareas:
            print(f"Nombre: {tarea[0]}, Detalles: {tarea[1]}, Estado: {tarea[2]}")
    else:
        print("No hay ninguna tareaa disponibles.")

def main():
    while True:
        mostrar_menu() 
        opcion = input("Ingrese el número de la opción que deseas a ejecutar: ")

        if opcion == "1":
            agrega_tarea()
        elif opcion == "2":
            elimina_tarea()
        elif opcion == "3":
            muestra_tareas()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta prnto chicos!")
            break 
        else:
            print("Estamos programando")

if __name__ == "__main__":
    main()