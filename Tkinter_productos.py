import tkinter as tk
#ahora creamos una ventana principal

ventana = tk.Tk()
ventana.title('Grupo 5__produtos')
ventana.geometry("600x400")#dimensiones de la ventana

#ahora creamos un label (texto no editable de identificación de la ventana)
etiqueta = tk.Label(ventana, text= "Elige tus productos favoritos",font="Arial")
#AHORA DEBO, SI O SI, EMPAQUETAR EL LABEL con lo siguiente:

etiqueta.pack()
#iniciamos este bucle necesario para mantener la ventana abierta...
ventana.mainloop()