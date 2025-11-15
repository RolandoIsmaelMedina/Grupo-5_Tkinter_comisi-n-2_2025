# MENU DESPLEGABLE

import tkinter as tk
ventana = tk.Tk()
ventana.title('Lista de producto')
ventana.geometry('1000x800')
ventana.configure(bg="#f0e6ff") 
ingreso_producto = tk.Entry(ventana)
ingreso_producto.pack()
ingreso_producto.configure(bg="#ffffff", fg="#4a0072")
def agregar_producto():
 producto = ingreso_producto.get()
 if producto:lista_producto.insert(tk.END, producto)
 ingreso_producto.delete(0, tk.END)
boton_agregar = tk.Button(ventana, text = 'Agregar producto', command = agregar_producto)
boton_agregar.pack()
boton_agregar.configure(bg="#4CAF50", fg="white")
def eliminar_producto():
 seleccion = lista_producto.curselection()
 if seleccion:lista_producto.delete(seleccion)
boton_eliminar = tk.Button(ventana, text = 'Eliminar producto', command = eliminar_producto)
boton_eliminar.pack()
lista_producto = tk.Listbox(ventana)
lista_producto.pack()

#MENU DESPLEGABLE


barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label =
'CONCESIONARIA', menu=menu_principal)
submenu = tk.Menu(menu_principal)
menu_principal.add_cascade(label =
'AUTOS', menu=submenu)
submenu.add_command(label = 'FORD')
submenu.add_command(label = 'PEUGEOT')


# barra de desplazamiento

marco = tk.Frame(ventana)
marco.pack(padx = 10, pady = 10)
scrollbar = tk.Scrollbar (marco)
scrollbar .pack(side = tk.RIGHT, fill =
tk.Y)
lista = tk.Listbox(marco, yscrollcommand
= scrollbar .set)
productos = ["remeras", "zapatos", "camisas", "medias", "zapatillas", "collares", "riñoneras","relojes", "alpargatas", "lentes de sol", "regalos", "sábanas", "fundas"]
for producto in productos:
 lista.insert(tk.END, producto)
scrollbar .config(command = lista.yview)

#RELOJ SIMPLE

import time
reloj = tk.Label(ventana, font =
('Arial', 60), bg = 'blue', fg = 'white')
def hora():
 tiempo_actual =time.strftime('%H:%M:%S')
 reloj.config(text = tiempo_actual)
 ventana.after(1000, hora)
reloj.pack(anchor = 'center')
hora()

ventana.mainloop()


