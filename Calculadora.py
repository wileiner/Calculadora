import tkinter as tk

# Crear una instancia de Tk, que es la ventana principal
ventana = tk.Tk()
ventana.title("Mi Calculadora")
ventana.configure(background= "#F0F8FF")
ventana.geometry("300x600")
ruta_icono = ('C:/Users/wilei/Documents/Calculadora/iconoCalculadora.ico')
ventana.iconbitmap(ruta_icono)

# Configurar el tamaño de las columnas y filas de la ventana
for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)
for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

# Visor de la entrada
visor = tk.StringVar()
entrada = tk.Entry(ventana, bd=5, 
                bg="lightblue", 
                fg="black", 
                font=("Arial", 20),
                width=30, 
                justify=tk.CENTER, 
                relief='raised',
                textvariable=visor,
                insertwidth=10)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones de la calculadora
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), (',', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

# Crear y posicionar cada botón
for (texto, fila, columna) in botones:
        tk.Button(ventana, 
                    text=texto,
                    padx=20,
                    pady=20,
                    font=("Arial", 20)
                    ).grid(
                            row=fila, 
                            column=columna,
                            sticky = 'nsew',
                    )

# boton de =
tk.Button(ventana, 
                    text='=',
                    padx=20,
                    pady=20,
                    font=("Arial", 20)
                    ).grid(
                            row=5, 
                            column=0,
                            columnspan=4,
                            sticky = 'nsew',
                    )

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
