
import tkinter as tk
ventana = tk.Tk()
ventana.title('Lista de producto')
ventana.geometry('1000x800')
ventana.configure(bg="#e6f7ff")
ingreso_producto = tk.Entry(ventana)
font=("Arial", 14)
ingreso_producto.pack()
ingreso_producto.configure(bg="#ffffff", fg="#4a0072")
def agregar_producto():
 producto = ingreso_producto.get()
 if producto:lista_producto.insert(tk.END, producto)
 ingreso_producto.delete(0, tk.END)
boton_agregar = tk.Button(ventana, text = 'Agregar producto', command = agregar_producto)
bg="#a3d9ff",  
    fg="#003044",
    font=("Arial", 12, "bold")
boton_agregar.pack()
boton_agregar.configure(bg="#4CAF50", fg="white")
def eliminar_producto():
 seleccion = lista_producto.curselection()
 if seleccion:lista_producto.delete(seleccion)
boton_eliminar = tk.Button(ventana, text = 'Eliminar producto', command = eliminar_producto)
bg="#ffb3b3",   
    fg="#5a0000",
    font=("Arial", 12, "bold")
boton_eliminar.pack()
boton_eliminar.configure(bg="#E53935", fg="white")
lista_producto = tk.Listbox(ventana)
font=("Arial", 16, "bold"),
    fg="#2b4e68",
    bg="#ffffff",
    width=35,
    height=8,
    highlightthickness=3,
    highlightbackground="#a3d9ff" 
lista_producto.pack()


barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label =
'BAZAR', menu=menu_principal)
submenu = tk.Menu(menu_principal)
menu_principal.add_cascade(label =
'PLATOS', menu=submenu)
submenu.add_command(label = 'PLATOS PLAYOS')
submenu.add_command(label = 'PLATOS HONDOS')


ventana.title('Tkinter proyecto grupo 5')
marco = tk.Frame(ventana)
marco.pack(padx = 10, pady = 10)
scrollbar = tk.Scrollbar (marco)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

lista = tk.Listbox(marco, yscrollcommand
= scrollbar.set)
productos = ["platos", "cuchillos", "tenedores", "cucharas", "tazas", "manteles", "individuales","pocillos", "teteras", "cafeteras", "repasadores", "jarras", "fuentes"]
for producto in productos:
 lista.insert(tk.END, producto)
lista.pack(side = tk.LEFT, fill = 
tk.BOTH)
scrollbar.config(command = lista.yview)


import time
reloj = tk.Label(ventana, font =
('Arial', 10), bg = 'grey', fg = 'white')
def hora():
 tiempo_actual =time.strftime('%H:%M:%S')
 reloj.config(text = tiempo_actual)
 ventana.after(1000, hora)
reloj.pack(anchor = 'center')
hora()

ventana.mainloop()










