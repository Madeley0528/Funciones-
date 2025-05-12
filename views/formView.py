import tkinter
from tkinter import messagebox  
from views.datosView import actualizarTabla

def form_view(ventana):
    formulario_panel = tkinter.Frame(ventana, bg="pink", width="300", height="600") 
    formulario_panel.grid(row=1, column=0, sticky="nsew")

    tabla_panel = tkinter.Frame(ventana, bg="white", width="50", height="60") 
    tabla_panel.grid(row=1, column=1, sticky="nsew")

    titulo = tkinter.Label(formulario_panel, text="Formulario de registro")
    titulo.pack(pady=5)

    entry = tkinter.Entry(formulario_panel)
    entry.pack(pady=5)

    def funcion_boton():
        respuesta = entry.get()
        actualizarTabla(f"SELECT * FROM datos_generales WHERE color ='{respuesta}'", tabla_panel)

    boton = tkinter.Button(formulario_panel, text="Enviar", command=funcion_boton)
    boton.pack(pady=5)

    #HORA
    titulo = tkinter.Label(formulario_panel, text="Filtrar por hora")
    titulo.pack(pady=5)

    entry_hora1 = tkinter.Entry(formulario_panel)
    entry_hora1.pack(pady=5)

    entry_hora2 = tkinter.Entry(formulario_panel)
    entry_hora2.pack(pady=5)

    def filtrar_por_hora():
        h1 = entry_hora1.get().strip()
        h2 = entry_hora2.get().strip()

        if not h1.isdigit() or not h2.isdigit():
            messagebox.showerror("Error", "Las horas deben ser valores numéricos.")
            return

        h1 = int(h1)
        h2 = int(h2)

        if h1 > h2:
            messagebox.showerror("Error", "La hora inicial no puede ser mayor que la final")
            return

        h1_formato = f"{h1:02d}:00"
        h2_formato = f"{h2:02d}:00"

        consulta = f"SELECT * FROM datos_generales WHERE hora_entrada BETWEEN '{h1_formato}' AND '{h2_formato}'"
        actualizarTabla(consulta, tabla_panel)

    boton_hora = tkinter.Button(formulario_panel, text="Enviar", command=filtrar_por_hora)
    boton_hora.pack(pady=5)

    actualizarTabla(f"SELECT * FROM datos_generales", tabla_panel)

     # Filtro de tarifa (mayor a el valor)
    titulo_tarifa = tkinter.Label(formulario_panel, text="Filtrar por Tarifa > valor")
    titulo_tarifa.pack(pady=5)

    entry_tarifa = tkinter.Entry(formulario_panel)
    entry_tarifa.pack(pady=5)

    def filtrar_tarifa_mayor():
        valor = entry_tarifa.get()
        if not valor.replace(".", "", 1).isdigit():
            messagebox.showerror("Error", "La tarifa debe ser un número.")
            return
        consulta = f"SELECT * FROM datos_generales WHERE tarifa > {valor}"
        actualizarTabla(consulta, tabla_panel)

    boton_tarifa_mayor = tkinter.Button(formulario_panel, text="Enviar", command=filtrar_tarifa_mayor)
    boton_tarifa_mayor.pack(pady=5)

        # Filtrar nombres que empiezen con una letra
    titulo_letra = tkinter.Label(formulario_panel, text="nombres que empiezan con letra...")
    titulo_letra.pack(pady=5)

    entry_letra = tkinter.Entry(formulario_panel)
    entry_letra.pack(pady=5)

    def filtrar_por_letra():
        letra = entry_letra.get().strip()

        if not letra.isalpha() or len(letra) != 1:
            messagebox.showerror("Error", "Debes escribir solo una letra.")
            return

        letra_mayus = letra.upper()
        consulta = f"SELECT * FROM datos_generales WHERE nombre LIKE '{letra_mayus}%'"
        actualizarTabla(consulta, tabla_panel)

    boton_letra = tkinter.Button(formulario_panel, text="Enviar", command=filtrar_por_letra)
    boton_letra.pack(pady=5)

    return formulario_panel



    